<?php
session_start();
//=============================================
// File.......: web_template.php
// Date.......: 2018-12-25
// Author.....: Benny Saxen
// Description:
//=============================================
// Configuration
//=============================================
// No configuration needed
//=============================================
$date         = date_create();
$ts           = date_format($date, 'Y-m-d H:i:s');
//=============================================
// library
//=============================================

//=============================================
function example($x)
//=============================================
{

}
//=============================================
// End of library
//=============================================


//=============================================
// Back-End
//=============================================
if (isset($_GET['do']))
{

  $do = $_GET['do'];

  if($do == 'something')
  {
    $dec = json_decode($json);

    for($idx = 0; $idx < count($dec); $idx++){
        $obj = (Array)$dec[$idx];
        echo $obj["name"];
    }
  }
}

if (isset($_POST['do']))
{
  $do = $_POST['do'];

  if ($do == 'anything')
  {

  }
}
//=============================================
// Front-End
//=============================================
echo "<html>
   <head>
      <title>InfoModel</title>
   </head>
   <body> ";

echo("<h1>Web Template</h1>");
echo ("<br><a href=infomodel.php?do=some&a=x>test_link</a>");

echo "<br><br>
   <table border=0>";
echo "
   <form action=\"#\" method=\"post\">
     <input type=\"hidden\" name=\"do\" value=\"send_message1\">
     <tr><td>A</td><td> <input type=\"text\" name=\"a\" value=$a></td>
     <tr><td>B</td><td> <input type=\"text\" name=\"b\" value=$b></td>
     <tr><td>C</td><td> <input type=\"text\" name=\"c\" ></td>
     <tr><td>D</td><td> <input type=\"text\" name=\"d\"></td>
     <td><input type= \"submit\" value=\"Send\"></td></tr>
   </form>
   </table>";
echo "<br><br>
      <table border=1>";
echo "
      <form action=\"#\" method=\"post\">
        <input type=\"hidden\" name=\"do\" value=\"send_message2\">
        <tr><td>A</td><td> <textarea rows=\"4\" cols=\"50\" name=\"comment\" form=\"usrform\">Enter text here...</textarea></td></tr>
        <tr><td>D</td><td> <input type=\"text\" name=\"d\"></td>
        <td><input type= \"submit\" value=\"Send\"></td></tr>
      </form>
      </table>";

echo ("<iframe src=http://81.224.182.81:3000 width=\"400\" height=\"300\"></iframe>");
//=============================================
// End of file
//=============================================
echo "</body></html>";
?>
