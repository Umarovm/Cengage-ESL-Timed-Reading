#!/usr/local/bin/perl

use CGI qw(param);
use Fcntl qw(:DEFAULT :flock);

$home_url = param("home_url");
$survey_name = param("survey_name");
$data_folder = $survey_name . "_data";
$style_css_file = $home_url . "style.css";
$code_js_file = $home_url . "code.js";

$gend_count = 2;
$ques_count = param("ques_count");
$resp_count = param("resp_count");
$user_location = param("location");
$user_gender = param("gender");

$error_flag = 0;
@data_array = (0);

print "Content-type: text/html\n\n";
print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n";
print "<html>\n";
print "  <head>\n";
print "    <link rel=\"stylesheet\" href=\"$style_css_file\" type=\"text/css\">\n";
print "    <script type=\"text/javascript\" language=\"javascript\" src=\"$code_js_file\"></script>\n";
print "  </head>\n";
if ($error_flag == 0){	&update_db();}
if ($error_flag == 0){	&thank_you();}
print "  </body>\n";
print "</html> <!-- 16 -->\n";

exit;

sub output_error
{
	print "  <body class='rwsBody'>\n";
	print "    <p><b><u><i>ERROR: " . @_[0] . "</i></u></b></p>\n";
	$error_flag = 1;
}

sub read_array
{
	my $gend, $ques, $resp, $data, @temp, $filepath;

	$filepath = $data_folder . "/" . @_[0] . ".dat";
	open(DATAFILE, "<" . $filepath)		|| &output_error("opening data file in log_selections::read_array()");
	#flock(DATAFILE, LOCK_SH)			|| &output_error("locking data file in log_selections::read_array()");
	for ($gend = 0; $gend < $gend_count; $gend ++)
	{
		for ($ques = 0; $ques < $ques_count; $ques ++)
		{
			$data = <DATAFILE>;
			@temp = split " ", $data;
			for ($resp = 0; $resp < $resp_count; $resp ++)
			{
				$data_array[$gend][$ques][$resp] = $temp[$resp];
			}
		}
		if ($gend < $gend_count - 1)
		{
			$data = <DATAFILE>;
		}
	}
	close DATAFILE						|| &output_error("closing data file in log_selections::read_array()");
}

sub thank_you
{
	print "  <body class='rwsBody' onload='top.main.error.location.replace(rootDir+\"survey_confirmed.htm\");'>\n";
	print "    <p>&nbsp;</p>\n";
	print "    <p align='center'>Your votes have been successfully recorded.</p>\n";
}

sub update_db
{
	my $ques;

	&read_array($user_location);
	for ($ques = 0; $ques < $ques_count; $ques ++)
	{
		$data_array[$user_gender][$ques][param("resp".($ques + 1))]++;
	}
	&write_array($user_location);
}

sub write_array
{
	my $gend, $ques, $resp, $filepath;

	$filepath = $data_folder . "/" . @_[0] . ".dat";
	sysopen(DATAFILE, $filepath, O_WRONLY | O_CREAT)	|| &output_error("opening data file in log_selections::write_array()");
	#flock(DATAFILE, LOCK_EX)							|| &output_error("locking data file in log_selections::write_array()");
	truncate(DATAFILE, 0)								|| &output_error("truncating data file in log_selections::write_array()");
	for ($gend = 0; $gend < $gend_count; $gend ++)
	{
		for ($ques = 0; $ques < $ques_count; $ques ++)
		{
			for ($resp = 0; $resp < $resp_count; $resp ++)
			{
				print DATAFILE $data_array[$gend][$ques][$resp];
				if ($resp < $resp_count - 1)
				{
					print DATAFILE " ";
				}
			}
			if ($ques < $ques_count - 1)
			{
				print DATAFILE "\n";
			}
		}
		if ($gend < $gend_count - 1)
		{
			print DATAFILE "\n\n";
		}
	}
	close DATAFILE										|| &output_error("closing data file in log_selections::write_array()");
}
