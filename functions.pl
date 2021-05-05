#!/usr/local/bin/perl5

#=================================================
#=
#= Duncan's Amazingly Useful Functions
#=
#= Developed by Duncan B. Sutherland III
#= For Houghton Mifflin
#= 2001 - 2002
#=
#=================================================

use CGI qw(:standard);

sub PrintHeader
{
local($headerfile) = @_;
#$headerfile = 'header.tpl';
open(HEADER, $headerfile);
flock(HEADER,$LOCK_SH);
while (
)
{
print "$_";
}

flock(HEADER,$LOCK_UN);
close(HEADER);
return;
}
##### END OF PRINTHEADER SUBROUNTINE

sub PrintFooter
{
local($footerfile) = @_;
#$footerfile = 'footer.tpl';
open(FOOTER, $footerfile);
flock(FOOTER,$LOCK_SH);
while (
)
{
print "$_";
}

flock(FOOTER,$LOCK_UN);
close(FOOTER);
return;
}
####### END OF PRINTFOOTER SUBROUNTINE


sub GetFileData
{
local($path) = @_;

if( open( FILE, "files/$path") )
{
while($buffer = )
{
$data .= $buffer;
}
}

$data =~ s/\n/
/g;

close(FILE);

return($data);
}



1; ## Just to make sure 0 isnt returned on the require call



	
