<STRUCTURETEMPLATE NAME="structure">
<HTML><HEAD><TITLE></TITLE>
<!-- scott g -->
<!--javascript popup script--><SCRIPT SRC="/shared/javascript/common_functions.js" LANGUAGE="JavaScript"></SCRIPT><!--javascript browser sensor--><SCRIPT SRC="/shared/javascript/platform.js" LANGUAGE="JavaScript"></SCRIPT><!--global style sheet--><LINK REL="stylesheet" HREF="/shared/css/hm_structure.css"><SCRIPT SRC="/shared/javascript/menu.js" LANGUAGE="JavaScript"></SCRIPT>
<STYLE TYPE="text/css">
 .popnavspace { background: url(/shared/images/popnav_space.gif) }
 .popnavsidespace { background: url(/shared/images/popnav_sidespace.gif) }
 .hmbannertile { background: url(/shared/images/tnav_hmbanner_tile_bg_pop.gif) }

</STYLE>

<STYLE>
 A{color:#003366; text-decoration:none}
</STYLE>

<script language="JavaScript">
<!--

ns4 = (document.layers)? true:false
ie4 = (document.all)? true:false

function init()
{
 	if (ns4) block = document.blockDiv
     if (ie4) block = blockDiv.style
                
}

// Show/Hide functions for pointer objects

function startReading(obj) 
{
 	sec = 20;
	timerID = setInterval("ShowTime()", 1000);

     if (ns4)
     {
     	 obj.visibility = "show"
     	
     }
     else if (ie4) obj.visibility = "visible"
}

function ShowTime()
{
	sec--;
	
	if(sec <  0)
	{
		clearInterval(timerID);
	  	window.status="Times Up";
	  	alert("Time is up, please click on the last read word in the text"); 
		return;
	}
		
	 window.status="Time Remaining: " + sec;
}                


//-->
</SCRIPT>   

</HEAD><BODY BGCOLOR="#ffffff" >

<TABLE BORDER="0" WIDTH="100%" CELLPADDING="0" CELLSPACING="0"><TR><TD><IMG ALT="Home" BORDER="0" WIDTH="203" HEIGHT="48" SRC="/shared/images/tnav_hmbanner_pop.gif"></TD><TD CLASS="hmbannertile" WIDTH="100%"> </TD><TD><IMG ALT="Home" BORDER="0" WIDTH="219" HEIGHT="48" SRC="/shared/images/tnav_hmbanner_collegediv_pop.gif"></TD>
</TR>
</TABLE>
<!--end global navigation-->


<!--start top navigation-->
<TABLE BORDER="0" WIDTH="100%" CELLPADDING="0" CELLSPACING="0">

<TR>
<TD WIDTH="121" HEIGHT="24" VALIGN="TOP">
<A ONMOUSEOUT="if (document.images) document.popnav_closewin.src= '/shared/images/popnav_closewin.gif';" ONMOUSEOVER="if (document.images) document.popnav_closewin.src= '/shared/images/popnav_closewin_on.gif';" HREF="javascript:self.close();"><IMG NAME="popnav_closewin" ALT="Close Window" BORDER="0" WIDTH="121" HEIGHT="24" SRC="/shared/images/popnav_closewin.gif"></A></TD>

<TD WIDTH="100%" HEIGHT="100%"><IMG ALT="" BORDER="0" WIDTH="100%" HEIGHT="24" SRC="/shared/images/popnav_space.gif"></TD></TR>
<!--<TR><TD><IMG ALT="" BORDER="0" WIDTH="18" HEIGHT="11" SRC="/shared/images/popnav_corner.gif"></TD>
<TD ALIGN="RIGHT"><IMG ALT="" BORDER="0" WIDTH="60" HEIGHT="11" SRC="/shared/images/popnav_hanger.gif"></TD>
</TR>--></TABLE> 

<!--end top navigation-->

<DIV CLASS=bodytext>
                                                                                       
