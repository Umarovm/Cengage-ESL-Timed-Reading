#!/usr/bin/which_perl -wT -- -M12

$|++;

use strict;

use DigitalV::Config;
use DigitalV::CourseProducts;
use DigitalV::CONTACT_FINDER_SUPPORT;
use DigitalV::Common qw(init_caching init_speedy);
use CGI;
use CGI::SpeedyCGI;
use Time::HiRes;
use CGI::Cache;
use DMV::Heartbeat;

use warnings;
use vars qw(
$persistent $cgi_cache $show_timings
$this_server $debug
);

$this_server = DigitalV::Config::server;
unless ( $this_server eq 'dev' ) {
$SIG{__WARN__} = sub { log_under_netscape(@_); };
$SIG{__DIE__} = sub {
log_under_netscape( 'DIE', @_ );
open( ERR,
'/inet/www/docs/wadsworth/wadgroup/restricted_access/server_error.html'
)
or die;
print CGI->header(), ;
exit;
};
} ## end unless ( $this_server eq 'dev')
$debug = 0;

unless ($persistent) {
if ($CGI::SpeedyCGI::i_am_speedy) {
$persistent = $CGI::SpeedyCGI::i_am_speedy;
init_speedy;
}
} ## end unless ($persistent)
DMV::Heartbeat::start_backend();

# Set to zero to disable timings.
# $show_timings = 0;
unless ( defined($show_timings) ) {
warn " Time::HiRes $Time::HiRes::VERSION\n";
$show_timings = 1;
}

# Set to zero to disable caching.
$cgi_cache = 0;
unless ( defined($cgi_cache) ) {
warn " CGI::Cache $CGI::Cache::VERSION\n";
$cgi_cache = 1;
}
init_caching('Wadsworth') if $cgi_cache; # Do this every time for groups.

my ( $t0, $from_cache );
$t0 = [Time::HiRes::gettimeofday()] if $show_timings;

my $q = CGI->new();
my $fid = $q->param('fid') || 'M0';
DMV::Heartbeat::start_request($fid);

#Redirect to alternate subroutine
$fid = 'M20b' if $fid eq 'M20';

# Cache by CGI parameters.
if ($cgi_cache) {
my $regen = $q->param('force_regenerate');
$q->delete('force_regenerate');
CGI::Cache::set_key( $q->Vars );
if ($regen) {
warn "Forcing regeneration of cache for this fid\n";
CGI::Cache::invalidate_cache_entry();
}

# Start caching -- output cached value if there is one.
unless ( CGI::Cache::start() ) {
$from_cache = 1;
goto Exeunt_Omnes;
}
} ## end if ($cgi_cache)

my %server = DigitalV::Config::getServerHash();
if ( $q->server_name() =~ /heinle/i ) {
$server{'discipline_templates'}{'0'} =
DigitalV::Config::heinle_document_root . '/pubco';
$server{'document_root'}{'0'} = DigitalV::Config::heinle_document_root;
} else {
$server{'discipline_templates'}{'0'} =
DigitalV::Config::wadsworth_document_root . '/pubco';
$server{'document_root'}{'0'} = DigitalV::Config::wadsworth_document_root;
}

$ENV{"PATH"} = "";
$ENV{'ORACLE_HOME'} = DigitalV::Config::db_home;
$ENV{'NLS_LANG'} = "american_america.we8iso8859p1";
$ENV{'HTML_TEMPLATE_ROOT'} = $server{'HTML_TEMPLATE_ROOT'} || '';

my @no_headers = (
qw( M40 M41test M42 M43 M44 M45 M46 M90 M35 M20bB M20bBI),
qw( M31 M33 M71 M72 M63 M692 M693), # Since we use sessions
qw( M70 M70b M68b M0 ), # We use redirects
);

my $skip_header = 0;
for my $target_fid (@no_headers) {
$skip_header = 1 if ( $fid eq $target_fid );
last if $skip_header;
}
print $q->header() unless $skip_header;

my $discipline_number = $q->param('discipline_number') || 0;
my %config = ( debug => $debug );

if ($discipline_number) {
my $path_to_cgi = $server{'path_to_cgi'}{$discipline_number};
$config{'action'} = join( '/', $path_to_cgi, DigitalV::Config::this_cgi );
$config{'instructor_action'} =
"$path_to_cgi/inst_course_resources/course_products_inst.pl";
} ## end if ($discipline_number)

my $dbh = DigitalV::CONTACT_FINDER_SUPPORT->new( server => \%server );
my $courseproducts = DigitalV::CourseProducts->new(
%server,
q => $q,
config => \%config,
dbfunc => $dbh,
db => $dbh->{'db'},
);

$courseproducts->$fid();

Exeunt_Omnes:
CGI::Cache::stop() if $cgi_cache;
if ($t0) {
my $elapsed = sprintf( "%1.3f", Time::HiRes::tv_interval($t0) );
if ($from_cache) {
warn "Cached fid = $fid; elapsed = $elapsed\n";
} else {
warn "Fid = $fid; elapsed = $elapsed\n";
}
} ## end if ($t0)

sub log_under_netscape {
DigitalV::Common::log_in_tmp('wadsworth', @_);
} ## end sub log_under_netscape
