# Cengage ESL Timed Reading
This source code was leaked by the exploitation of a [directory traversal](https://college.cengage.com/cgi-bin/esl_site/timed_reading/timed_reading.cgi?unit01/../../../../../../../../etc/passwd) (CWE-23) on line 38 of timed_reading.cgi, when $dataArray[0] isn't validated before it is used as an argument in the call to GetFileData().

This was developed by Duncan B. Sutherland III in February 2002.

The HTML and JS files are not included because they can just be viewed through "view-source:". These are just the files for the server-sided code and the files that are generally not visible to the user.
