<html>

	<head>
		<h>'Venue: '<?php echo $_POST["venue"]; ?></h>
	</head>
	
	<br>
	<body>
	<br>
	<br>
	<p1>Select your author.</p1>
	<br>


	<form id= 'options' action="http://titan.dcs.bbk.ac.uk/~friver01/collaborationoutcome.php" method="get">
	<form id= 'options' action="collaborationoutcome.php" method="post">

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
	  $aAuthor = $_POST['prof'];
	  
	  	  
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
		  echo($aAuthor[$i] . " ");
		}
	  }
	?>
	
	<br>

	<br>
	
	<table>
		<tr>
			<td><td>
			<?php
			foreach ($aAuthor as $value) {
			echo '<th scope ='.'col'.'>'.$value.'</th>';
			}
			?>

		</tr>
		
		<?php
		foreach ($aAuthor as $value) {
		echo '<tr> <th scope ='.'row'.'>'.$value.'</th></tr>';
		}
		?>

		<tbody>
		
		<?php
		foreach ($aAuthor as $value) {
		echo '<td>'.'0'.'</td>';
		}
		?>		
		</tbody>
		



	</table>
	
	<br>
	
	<?php
		
		foreach ($aAuthor as $value) {
		echo "$value <br>";
		}
	?>
	


</html>