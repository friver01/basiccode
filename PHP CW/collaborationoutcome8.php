<html>

	<head>
		<link rel="stylesheet" type="text/css" href="mystyle.css">
	</head>

	<!-- I include this heading that retrieves the venue value populated in 
	the former text form. I use the $_GET method.
	-->	
	<br>
	<body>
		<h1>Venue: <?php echo $_GET["venue"]; ?></h1>
	<br>
	<!-- Here I replicate the former html code so it will appear again when
	the submission is done. I have included it so I can populate data in the same
	screen in case the user wants to run several consultations or simply if a value
	is forgotten.
	-->	

	<br>
	<p1>Select your author.</p1>
	<br>


	<form id= 'options' action="http://titan.dcs.bbk.ac.uk/~friver01/collaborationoutcome8.php" method="get">

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

		<br>
		<br>
		
		<input type="text" name="venue" maxlength="50" />Introduce a Venue<br />

		<br>

		<input type="submit" name="formSubmit" value="Submit" />

	</form>
	
	</body>

	<!-- I am including two associative arrays so I can transform the data taken
	from the checkboxes (authors identifiers) into their names or the files the are 
	linked to.
	-->	
	
	<?php
	  
		$names = array('p/APoulovassilis'=> 'Alex', 'c/AndreaCali'=> 'Andrea', 'h/JanHidders'=>'Jan', 'l/MarkLevene'=>'Mark', 'm/NigelJMartin'=>'Nigel', 'w/PeterTWood'=>'Peter'); 
		$source = array('p/APoulovassilis'=> 'Poulovassilis-Alexandra.xml', 'c/AndreaCali'=> 'Cali-Andrea.xml', 'h/JanHidders'=>'Hidders-Jan.xml', 'l/MarkLevene'=>'Levene-Mark.xml', 'm/NigelJMartin'=>'Martin-Nigel.xml', 'w/PeterTWood'=>'Wood-Peter.xml');
		
		# I use isset to check if some values have been ticked in the checkboxes
	  
		if(isset($_GET['prof'])) 
			{
			# Here I link the list of values retrieved with the $_GET method to a variable $aAuthor
			
			$aAuthor = $_GET['prof'];
			
			# I create two empty arrays where I will include the names and files selected once I will tranform the
			# checkbox value (pid) into their associated ones. Everytime I will run the code it will firstly clear the 
			# array and afterwards append the new values using array_push
			
			$namesselected = [];
			$namesselected = array();

			$sourceselected = [];
			$sourceselected = array();
			
			# Here I simply count the number of authors, have their names printed and append them to $nameselected array
			# I printed them twice just for my internal checking.
			
			$N = count($aAuthor);

			echo("You selected $N author(s): ");
		
			for($i=0; $i < $N; $i++)
			{
			echo($names[$aAuthor[$i]] . ", ");
			array_push($namesselected,$names[$aAuthor[$i]]);
			}
			
			foreach ($namesselected as $value){
				echo '<p>'.$value.'</p>';
				}

			# I repeat the same operation to retrieve the files linked to the differente authors.

			$N = count($aAuthor);

			echo("You selected $N source(s): ");
		
			for($i=0; $i < $N; $i++)
			{
			echo($source[$aAuthor[$i]] . ", ");
			array_push($sourceselected,$source[$aAuthor[$i]]);
			}
			
			foreach ($sourceselected as $value){
				echo '<p>'.$value.'</p>';
				}				
	
			}
			
		# Finally if there are no checkboxes ticked I print an error message and finish with exit()			
						
		
		else
			{
			echo("<p> You didn't select any author. Try Again.</p>");
			exit();	
			} 
	?>
	
	<br>
	<br>
	<br>

	<!-- PART 4 (A). Function to retrieve data in each added cell
	As explained later the variables to consider in the function are the xml file 
	included in the array $sourceselected and the pid identifier included as a value
	-->	 
	
	<?php
	
	function retrievecollaboration(){
		$xmlDoc = new DOMDocument;
		$xmlDoc->load('http://titan.dcs.bbk.ac.uk/~friver01/Poulovassilis-Alexandra.xml');;
		$xpath = new DOMXPath($xmlDoc);
#		$query ='count(//author[contains(@pid,'p/APoulovassilis')/text()]')';
#		$query ='count(//author[@pid ='p/APoulovassilis'])';
#		$elements = $xpath->evaluate('count(//author[@pid ='p/APoulovassilis'])');
#		echo $elements;

	}
		

	?>
	
	<?php
		$xmlDoc = new DOMDocument;
		$xmlDoc->load('http://titan.dcs.bbk.ac.uk/~friver01/Poulovassilis-Alexandra.xml');;
		$xpath = new DOMXPath($xmlDoc);
		$query ='//author[@pid]';
		$elements1 = $xpath->query($query);
		$total = count($elements1);
		echo $total;
	
	?>	
	
	<?php
		$xmlDoc = new DOMDocument;
		$xmlDoc->load('http://titan.dcs.bbk.ac.uk/~friver01/Poulovassilis-Alexandra.xml');;
		$xpath = new DOMXPath($xmlDoc);
		$authorid = $xmlDoc->getElementsByTagName('author')
#		$query =count(string (//author[@pid ='p/APoulovassilis']))';
#		$elements1 = $xpath->evaluate($query,$authorid);
#		$total = count($elements1);
#		echo $elementsl;
	
	?>	
	
	<!-- PART 4 (B). Function to retrieve data in each added cell when the venue is chosen by the user
	In this case I will include an additional condition in the query so that the venue equals the textbox previously populated.
	-->	
	
	<br>
	<br>
	<br>
	<?php
		if (isset ($_GET["venue"])) {
			$xmlDoc = new DOMDocument;
			$xmlDoc->load('http://titan.dcs.bbk.ac.uk/~friver01/Poulovassilis-Alexandra.xml');;
			$xpath = new DOMXPath($xmlDoc);
			$authorid = $xmlDoc->getElementsByTagName('author')
	#		$query =count(string (//author[@pid ='p/APoulovassilis']))';
	#		$elements1 = $xpath->evaluate($query,$authorid);
	#		$total = count($elements1);
	#		echo $elementsl;
		}
	
		else
		{
		echo("<p> You didn't select any venue.</p>");
		exit();	
		} 
	
	
	
	
	
	?>		
	
	
	
	
	

	<!-- Now I create the table where the values selected and the values retrieved from the
	xml files are displayed. As it is a double-entry table I create headers for columns and rows
	using the scope attribute.
	-->	
	
	<table>
		<tr>
			<!-- I include and empty data cell to prepare the table headers.-->	
			<td></td>
			<?php
				# I loop in the former selected names array to populate the header.
				foreach ($namesselected as $value) {
				echo '<th scope ='.'col'.'>'.$value.'</th>';
				}
			?>	

		</tr>
		
		<?php
		# I repeat the same operation with the row headers .
		foreach ($namesselected as $value) {
			echo '<tr> <th scope ='.'row'.'>'.$value.'</th>';
				# and additionally I add for each header row, data rows depending on the checkbox ticked
				foreach ($aAuthor as $value) {
					# here I add the value of each data cell. To retrieve data from the XML file I will use XML DOC
					# and XPath. Each data is given by a function that depends on at least two variables: the xml file I have to load (value from sourceselected)
					# to retrieve data and the pid identifier $value from $aAuthor that it is associated to the author attribute. Additionally in case of
					# selecting a venue, there are two checks that have to be done: firstly if the textbox populated is included in the list of venues of 
					# the xml file and secondly I will use the operator and when evaluating the query to choose only the collaborations for the venue
					# selected.
					
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