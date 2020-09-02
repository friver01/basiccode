<html>

	<head>
		<link rel="stylesheet" type="text/css" href="mystyle.css">
	</head>
	
	<br>
	<body>
		<h1>Venue: <?php echo $_GET["venue"]; ?></h1>
	<br>
	<br>
	<p1>Select your author.</p1>
	<br>


	<form id= 'options' action="http://titan.dcs.bbk.ac.uk/~friver01/collaborationoutcome3.php" method="get">

		<input type="checkbox" id="author1" name="prof[]" value="p/APoulovassilis">
		<label for="author1"> Alex</label><br>
		<input type="checkbox" id="author2" name="prof[]" value="c/AndreaCali">
		<label for="author2"> Andrea</label><br>
		<input type="checkbox" id="author3" name="prof[]" value="h/JanHidders">
		<label for="author3"> Jan</label><br>		
		<input type="checkbox" id="author4" name="prof[]" value="l/MarkLevene">
		<label for="author4"> Mark</label><br>
		<input type="checkbox" id="author5" name="prof[]" value="m/NigelJMartin">
		<label for="author5"> Nigel</label><br>
		<input type="checkbox" id="author6" name="prof[]" value="w/PeterTWood">
		<label for="author6"> Peter</label><br>		
		
		<input type="text" name="venue" maxlength="50" />Introduce a Venue<br />

		<input type="submit" name="formSubmit" value="Submit" />

	</form>
	
	</body>
	
		<?php
	  $aAuthor = $_GET['prof'];
	  
	  $names = array('p/APoulovassilis'=> 'Alex', 'c/AndreaCali'=> 'Andrea', 'h/JanHidders'=>'Jan', 'l/MarkLevene'=>'Mark', 'm/NigelJMartin'=>'Nigel', 'w/PeterTWood'=>'Peter'); 
	  $source = array('p/APoulovassilis'=> 'Poulovassilis-Alexandra.xml', 'c/AndreaCali'=> 'Cali-Andrea.xml', 'h/JanHidders'=>'Hidders-Jan.xml', 'l/MarkLevene'=>'Levene-Mark.xml', 'm/NigelJMartin'=>'Martin-Nigel.xml', 'w/PeterTWood'=>'Wood-Peter.xml');
	  
	  
	  if(empty($aAuthor)) 
	  {
		echo("You didn't select any author.");
	  } 
	  else
	  {
		$N = count($aAuthor);

		echo("You selected $N author(s): ");
		
		for($i=0; $i < $N; $i++)
		{
		  echo($names[$aAuthor[$i]] . " ");
		}
	  }
	?>
	
	<br>
	
	<?php
		$N = count($aAuthor);

		echo("You selected $N source(s): ");
		
		for($i=0; $i < $N; $i++)
		{
		  echo($source[$aAuthor[$i]] . " ");
		}
	
	
	?>
	<br>
	<br>
	

	<br>
	<br>
	<br>
	
	<table>
		<tr>
			<td></td>
			<?php
				foreach ($aAuthor as $value) {
				echo '<th scope ='.'col'.'>'.$value.'</th>';
				}
			?>	

		</tr>
		
		<?php
		foreach ($aAuthor as $value) {
			echo '<tr> <th scope ='.'row'.'>'.$value.'</th>';
				foreach ($aAuthor as $value) {
					echo '<td>'.$value.'</td>';
					}
			echo '</tr>';
			}
		?>

		<tbody>
		
	
		</tbody>
		



	</table>
	
	<br>
	
	<?php
		
		foreach ($aAuthor as $value) {
		echo "$value <br>";
		}
	?>
	


</html>