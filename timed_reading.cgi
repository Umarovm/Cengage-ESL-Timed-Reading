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

$dataFile = $ENV{'QUERY_STRING'};

## Initialize HTML stuff
print header;
print start_html;
&PrintHeader("header.tpl");

@dataArray = split(/::/, $dataFile);

$text = GetFileData($dataArray[0]);

@wordArray = split(/ /, $text);

$total = @wordArray;

print("@wordArray");

print("<FORM NAME=form2><INPUT TYPE=button NAME=button2 VALUE=\"Click Here When Finished\" onClick=\"javascript:Results($total, '$dataFile');\">");
print("</FORM>");  

&PrintFooter("footers/footer.tpl");

#### END OF MAIN #################################################
