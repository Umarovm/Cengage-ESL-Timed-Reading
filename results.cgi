#!/usr/local/bin/perl5

#=================================================
#=
#= ESL Timed Reading
#=
#= Developed by Duncan B. Sutherland III
#= For Houghton Mifflin
#= Feb 2002
#=
#= Description:
#=
#=================================================

use CGI qw(:standard);

require "functions.pl";



#### GLOBALS #############################################



#### BEGIN MAIN PROGRAM ##############################

##read(STDIN, $buffer, $ENV{'QUERY_STRING'}); ##

$data = $ENV{'QUERY_STRING'};

@dataArray = split(/::/, $data);

if($dataArray[0] != 0)
{
$wpm = ($dataArray[1] * 60) / $dataArray[0];
}
else
{
$wpm = 0;
}

$wpm2 = sprintf("%.2d", $wpm);

## Initialize HTML stuff
print header;
print start_html;
&PrintHeader("header2.tpl");

print("<B>Results: $wpm2 word(s) / minute</B>");

print("<BR><BR>Click on the NEXT button to answer the comprehension questions about what you read.<BR>");

print("<FORM NAME=form1><INPUT TYPE=button NAME=button1 VALUE=\"Next >>\" onClick=\"document.location='$dataArray[3]'\"></FORM>");

&PrintFooter("footer.tpl");

#### END OF MAIN #################################################
