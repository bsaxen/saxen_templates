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
function generateHtml($inp)
//=============================================
{
  $jsonIterator = new RecursiveIteratorIterator(new RecursiveArrayIterator(json_decode($inp, TRUE)),RecursiveIteratorIterator::SELF_FIRST);
  echo("<table border=1>");
  foreach ($jsonIterator as $key => $val) {
      if(is_array($val)) {
          echo "<tr><td>$key</td><td></td></tr>";
      } else {
          //echo "     $key = $val";
          if($val != -1)echo "<tr><td>$key</td><td>$val</td><tr>";
      }
   }
   echo "</table>";
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

  }
}

if (isset($_POST['do']))
{
  $do = $_POST['do'];

  if ($do == 'generateHtml')
  {
    echo("b1");
      $json = $_POST['json'];
      //echo("$json");
      $d = $_POST['d'];
      echo("$d");
      generateHtml($json);
  }
  if ($do == 'abcd')
  {
    echo("b1");
      $a = $_POST['a'];
      echo("$a");
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
     <input type=\"hidden\" name=\"do\" value=\"abcd\">
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
      <form action=\"#\" method=\"post\" name=\"jjss\">
        <input type=\"hidden\" name=\"do\" value=\"generateHtml\">
        <tr><td>A</td><td> <textarea name=\"json\" rows=\"4\" cols=\"50\" >Enter text here...</textarea></td></tr>
        <tr><td>D</td><td> <input type=\"text\" name=\"d\"></td>
        <td><input type= \"submit\" value=\"Send\"></td></tr>
      </form>
      </table>";

echo ("<iframe src=http://asdasd:3000 width=\"400\" height=\"300\"></iframe>");
//=============================================
// End of file
//=============================================
echo "</body></html>";
?>
