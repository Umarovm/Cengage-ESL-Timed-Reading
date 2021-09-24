#!/usr/local/bin/perl

use CGI qw(param);
use Fcntl qw(:DEFAULT :flock);

$home_url = param("home_url");
$survey_name = param("survey_name");
$survey_def_file = $survey_name . ".def";
$style_css_file = $home_url . "style.css";
$code_js_file = $home_url . "code.js";
$gr_folder = $home_url . "gr";

$ques_count = 0;
$resp_count = 0;
@ques_text = ("x");

$error_flag = 0;

print "Content-type: text/html\n\n";
print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n";
print "<html>\n";
print "  <head>\n";
print "    <link rel=\"stylesheet\" href=\"$style_css_file\" type=\"text/css\">\n";
print "    <script type=\"text/javascript\" language=\"javascript\" src=\"$code_js_file\"></script>\n";
print "  </head>\n";
print "  <body class='rwsBody'>\n";
if ($error_flag == 0){	&read_def();}
if ($error_flag == 0){	&output_body();}
print "  </body>\n";
print "</html>\n";

exit;

sub read_def
{
	my $inQues = 0;
	my $data;
	open (DEF_FILE, $survey_def_file)	|| &output_error("opening definition file in read_def()");
	#flock(DEF_FILE, LOCK_SH)			|| &output_error("locking definition file in read_def()");

	# read number of responses
	$resp_count = <DEF_FILE>;
	chomp($resp_count);

	# read questions
	while (($data = <DEF_FILE>) && ($error_flag == 0))
	{
		chomp($data);
		if (index($data, "<ITEM>") > -1)
		{
			if ($inQues == 1)
			{
				&output_error("&lt;ITEM&gt; without closing &lt;/ITEM&gt;.");
			}
			else
			{
				$inQues = 1;
				$ques_count ++;
				$ques_text[ques_count] = "";
			}
		}
		elsif (index($data, "</ITEM>") > -1)
		{
			if ($inQues == 0)
			{
				&output_error("&lt;/ITEM&gt; without opening &lt;ITEM&gt;.");
			}
			else
			{
				$inQues = 0;
			}
		}
		else
		{
			if ($inQues == 1)
			{
				$ques_text[$ques_count] .= $data;
			}
		}
	}
	close DEF_FILE						|| &output_error("closing definition file in read_def()");
}

sub output_body
{
	my $chkd, $ques, $resp;

	&output_first_part();

	# first row
	print "  <table border='1' cellpadding='5' width='97%' align='center'>\n";
	print "    <tr valign='bottom'>\n";
	print "      <td class='rwsTableHead'>\n";
	print "        <p class='rwsTableHead'><img src='$gr_folder/head_questions.gif' alt='' border='0'></p>\n";
	print "      </td>\n";
	for ($resp = 1; $resp <= $resp_count; $resp++)
	{
		print "      <td class='rwsTableHead' align='center'>\n";
		print "        <p class='rwsTableHead'><img src='$gr_folder/head_choice_$resp.gif' alt='' border='0'></p>\n";
		print "      </td>\n";
	}
	print "    </tr>\n";
	
	# second and following rows
	for ($ques = 1; $ques <= $ques_count; $ques++)
	{
		print "    <tr valign='middle'>\n";
		print "      <td class='rwsTable'>\n";
		print "        $ques_text[$ques]\n";
		print "      </td>\n";
		for ($resp = 0; $resp < $resp_count; $resp++)
		{
			$chkd = "";
			print "      <td class='rwsTable' align='center'>\n";
			print "        <input type='radio' name='resp$ques' value='$resp'$chkd>\n";
			print "      </td>\n";
		}
		print "    </tr>\n";
	}
	
	# close table
	print "  </table>\n";
	
	&output_last_part();
}

sub output_error
{
	print "    <p><b><u><i>ERROR: " . @_[0] . "</i></u></b></p>\n";
	$error_flag = 1;
}

sub output_first_part
{
print <<END_first_part;
<form action="/cgi-wadsworth/rws/log_selections.cgi" name="dataEntry">
  <input type="hidden" name="survey_name" value="$survey_name">
  <input type="hidden" name="home_url" value="$home_url">
  <input type="hidden" name="ques_count" value="$ques_count">
  <input type="hidden" name="resp_count" value="$resp_count">
  <input type="hidden" name="submitted" value="0">
  <table border="0" cellpadding="5" width="97%" align="center">
    <tr>
      <td>
        <img src="$gr_folder/label_gender.gif" alt="" border="0">
        

        <em class="rwsCtrl"><input type="radio" name="gender" value="0">Male <input type="radio" name="gender" value="1">Female</em>


      </td>
    </tr>
    <tr>
      <td>
        <img src="$gr_folder/label_location.gif" alt="" border="0">
        

        <select name="location"> 
          <option value="__">Select location...</option>
          <option value="AL">Alabama</option>
          <option value="AK">Alaska</option>
          <option value="AZ">Arizona</option>
          <option value="AR">Arkansas</option>
          <option value="CA">California</option>
          <option value="CO">Colorado</option>
          <option value="CT">Connecticut</option>
          <option value="DE">Delaware</option>
          <option value="FL">Florida</option>
          <option value="GA">Georgia</option>
          <option value="HI">Hawaii</option>
          <option value="ID">Idaho</option>
          <option value="IL">Illinois</option>
          <option value="IN">Indiana</option>
          <option value="IA">Iowa</option>
          <option value="KS">Kansas</option>
          <option value="KY">Kentucky</option>
          <option value="LA">Louisiana</option>
          <option value="ME">Maine</option>
          <option value="MD">Maryland</option>
          <option value="MA">Massachusetts</option>
          <option value="MI">Michigan</option>
          <option value="MN">Minnesota</option>
          <option value="MS">Mississippi</option>
          <option value="MO">Missouri</option>
          <option value="MT">Montana</option>
          <option value="NE">Nebraska</option>
          <option value="NV">Nevada</option>
          <option value="NH">New Hampshire</option>
          <option value="NJ">New Jersey</option>
          <option value="NM">New Mexico</option>
          <option value="NY">New York</option>
          <option value="NC">North Carolina</option>
          <option value="ND">North Dakota</option>
          <option value="OH">Ohio</option>
          <option value="OK">Oklahoma</option>
          <option value="OR">Oregon</option>
          <option value="PA">Pennsylvania</option>
          <option value="RI">Rhode Island</option>
          <option value="SC">South Carolina</option>
          <option value="SD">South Dakota</option>
          <option value="TN">Tennessee</option>
          <option value="TX">Texas</option>
          <option value="UT">Utah</option>
          <option value="VT">Vermont</option>
          <option value="VA">Virginia</option>
          <option value="WA">Washington</option>
          <option value="WV">West Virginia</option>
          <option value="WI">Wisconsin</option>  
          <option value="WY">Wyoming</option>
          <option value="__">----------</option>
          <option value="XX">Outside the United States</option>
        </select> 
        

        

      </td>
    </tr>
    <tr>
      <td>
        <img src="$gr_folder/label_votes.gif" alt="" border="0">
      </td>
    </tr>
  </table>
END_first_part
}

sub output_last_part
{
print <<END_last_part;
  <center>
    

    <p class="rwsBody">
      <input type="button" name="voteButton" value="Submit My Data" onclick="if(formCheck(self.document.forms[0])){self.document.forms[0].submit();}"> 
    </p>
  </center>
</form>
END_last_part
}
