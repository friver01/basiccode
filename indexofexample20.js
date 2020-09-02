/* The HTML file associated with this file can be reach in Birkbeck CS Department server at
https://titan.dcs.bbk.ac.uk/~friver01/TESTJSPATHINDEX20
-->
In the server you can find also the different versions of the code written to produce this solution with the 
different steps and the timestamps when the file was last modified.
*/



$('#categories').change (function () {
	$('#div2').empty();
	$('#div1').empty();
	var share = $('#share option:selected').text();
	var surname = document.getElementById("surname").value;
	var year = document.getElementById("addressYear").value;
	var category = $('#categories option:selected').text();
	var parameteryear = $('#parameter1 option:selected').text();
	var parametershare = $('#parameter2 option:selected').text();	
	alert('Your category: '+ category ); 
	$('#div2').append ('<ol>'+'Category:'+' ' + category + '  '+'</ol>'+'<ol>' +'Year: ' + parameteryear + year  +'   '+'</ol>'
	+'<ol>'+'Share: ' + parametershare +share  + '    '+'</ol>' +'<ol>' +'Surname Search: ' + surname+'</ol>');

 });

/* I use jQuery .change method to detect changes in the user input. Basically everytime the user modifies a field
I clear the input and output parts of the HTML and I define the variables populates. Depending on the field I take either
the text or the value associates with each field. I have introduced an alert to control errors so the user can double-checked
the input. In the case of Years I have additionally introduced a hint to avoid years not included in the dataset.

Finally I add in the input partition different <ol> elements with the data that will be searched in the json file to
produce the output.

This patern is repeated with the 6 variables that can be populated as requested in the Coursework.
*/

$('#addressYear').change (function () {
	$('#div2').empty();
	$('#div1').empty();
	var share = $('#share option:selected').text();
	var surname = document.getElementById("surname").value;
	var year = document.getElementById("addressYear").value;
	var category = $('#categories option:selected').text();
	var parameteryear = $('#parameter1 option:selected').text();
	var parametershare = $('#parameter2 option:selected').text();
	if (year < 1901 || year > 2017) {
		alert ('Year not valid \n  Should be between 1901 and 2017!');
		
		} else {
	alert('Your year: '+ parameteryear +year ); 
	$('#div2').append ('<ol>'+'Category:'+' ' + category + '  '+'</ol>'+'<ol>' +'Year: ' + parameteryear + year  +'   '+'</ol>'
	+'<ol>'+'Share: ' + parametershare +share  + '    '+'</ol>' +'<ol>' +'Surname Search: ' + surname+'</ol>');
		}
	
	
 });

$('#share').change (function () {
	$('#div2').empty();
	$('#div1').empty();
	var share = $('#share option:selected').text();
	var surname = document.getElementById("surname").value;
	var year = document.getElementById("addressYear").value;
	var category = $('#categories option:selected').text();
	var parameteryear = $('#parameter1 option:selected').text();
	var parametershare = $('#parameter2 option:selected').text();	
	alert('Your share: '+ parametershare + share ); 
	$('#div2').append ('<ol>'+'Category:'+' ' + category + '  '+'</ol>'+'<ol>' +'Year: ' + parameteryear + year  +'   '+'</ol>'
	+'<ol>'+'Share: ' + parametershare +share  + '    '+'</ol>' +'<ol>' +'Surname Search: ' + surname+'</ol>');
 	
	
 }); 

$('#parameter1').change (function () {
	$('#div2').empty();
	$('#div1').empty();
	var share = $('#share option:selected').text();
	var surname = document.getElementById("surname").value;
	var year = document.getElementById("addressYear").value;
	var category = $('#categories option:selected').text();
	var parameteryear = $('#parameter1 option:selected').text();
	var parametershare = $('#parameter2 option:selected').text();	
	alert('Your year: '+ parameteryear + year ); 
	$('#div2').append ('<ol>'+'Category:'+' ' + category + '  '+'</ol>'+'<ol>' +'Year: ' + parameteryear + year  +'   '+'</ol>'
	+'<ol>'+'Share: ' + parametershare +share  + '    '+'</ol>' +'<ol>' +'Surname Search: ' + surname+'</ol>');
 	
	
 });

$('#parameter2').change (function () {
	$('#div2').empty();
	$('#div1').empty();
	var share = $('#share option:selected').text();
	var surname = document.getElementById("surname").value;
	var year = document.getElementById("addressYear").value;
	var category = $('#categories option:selected').text();
	var parameteryear = $('#parameter1 option:selected').text();
	var parametershare = $('#parameter2 option:selected').text();	
	alert('Your share: '+ parametershare + share ); 
	$('#div2').append ('<ol>'+'Category:'+' ' + category + '  '+'</ol>'+'<ol>' +'Year: ' + parameteryear + year  +'   '+'</ol>'
	+'<ol>'+'Share: ' + parametershare +share  + '    '+'</ol>' +'<ol>' +'Surname Search: ' + surname+'</ol>');
 	
	
 });
 
$('#surname').change (function () {
	$('#div2').empty();
	$('#div1').empty();
	var share = $('#share option:selected').text();
	var surname = document.getElementById("surname").value;
	var year = document.getElementById("addressYear").value;
	var category = $('#categories option:selected').text();
	var parameteryear = $('#parameter1 option:selected').text();
	var parametershare = $('#parameter2 option:selected').text();	
	alert('Your searched surname string: ' +surname+  '\n  Case sensitive search!' ); 
	$('#div2').append ('<ol>'+'Category:'+' ' + category + '  '+'</ol>'+'<ol>' +'Year: ' + parameteryear + year  +'   '+'</ol>'
	+'<ol>'+'Share: ' + parametershare +share  + '    '+'</ol>' +'<ol>' +'Surname Search: ' + surname+'</ol>');
 	
	
 }); 


button.addEventListener("click",retrieve); 

/* I use addEventListener and have it associated with a function to retrieve the json data once I clicck in the results
button. I prefer this method rather that the onclick javascript one because it avoids triggering undesired events and can
be linked to more than one variable.

Then I define the retrieve function where I use jQuery $.getJson method to gather the input data across the file. I have left
some comments in places where I used alerts to control the type of data. One of this points is when I had to define the 
string path to be introduced in the JSPath.apply JsPath method. Basically I gather again the populated fields using the 
text or the document.getElementById JS command and link them in a variable called path as explained in the JSPath GitHub
instructions. I used as well this onlin resource http://www.jsonquerytool.com/  that allowed me to check the outcome of the path income in some Json
code.

This JSPath.apply method simplified the original json data only selecting those relevant for the input searched. I include 
the result of the method in a variable called winners that includes an Json Data object. 
*/

function retrieve() { 
	$.getJSON('nobel.json', function(data) {

		var share = $('#share option:selected').text();
		var category = $('#categories option:selected').text();
		var year = document.getElementById("addressYear").value;
		var compare = document.getElementById("surname").value;
		var parameteryearsel = document.getElementById("parameter1").value;
		var parametersharesel = document.getElementById("parameter2").value;
//		alert (typeof parametersharesel);
//		alert (parametersharesel);
		var path = '.prizes{.year'+ parameteryearsel+ '\''+year+'\' &&.category *=\''+category
		+'\'  &&..surname *= \''+compare+'\'&&..share'+ parametersharesel+ ' \''+share+'\'}';	

//		alert (typeof path);
//		alert (path);
		var comparison = {
			'*=': function (x, y) { return x === y },
			'>=': function (x, y) { return x >= y },
			'<=': function (x, y) { return x <= y }
				};
			
		var winners = JSPath.apply(path, data);

/* Once I have the relevant data in this variable I applied the $each method to produce 2 loops (one embedded into other, this 
was somehow tricky).

Firstly I loop over the prizes first children level (year, category and laureates) and add a table header on each relevant
data. Secondly, inside each laurate I loop on the rest of data (firstname, surname, share, motivation, id).

This second loop, when one of the laurates values happened to be true, added the rest of children of the laurate value to 
the output. To avoid this, I have introduced a if condition that checks 3 possibilities before appending the data to the
output: I compare if substrings have been populated using indexOf as suggested in the coursework instructions. I have to 
convert the json object into a string to produce the comparison.

Secondly, regarding the share data I define a comparison variable that allows me to compare the share populated input with
the share value of every data and additionally I include in the comparison the parameter option selected by the user.
This variable allows me to introduce dinamically this condition in the comparison before adding the all child data in the
same level to the outcome    
*/


		$.each (winners, function (key, value) {
			$tableparent = '<table class = "awards"> <thead> Award </thead> <thead> <th> Year </th> <th> Category </th> </thead> </table>';
			$('#div1').append('<br>');
			$('#div1').append($tableparent);
			$('#div1').append('<tr>' + '<td>' + value.year + '</td>' +
				"<td>" + value.category + '</td>'+"</tr>"+'<tr>'+'</tr>'+'<br>');
				$tablechildren = '<table class = "laureates"> <thead> Laureates </thead> <thead> <th> First Name </th> <th> Surname </th> </thead> </table>';
				$('#div1').append($tablechildren);
					$.each(value.laureates, function(index, obj){
						var checktext = JSON.stringify (obj.surname);
						var i = checktext.indexOf(compare);
	//					alert (comparison [$('#parameter2 option:selected').val()](obj.share , share));
	//					alert (i);
	//					alert (obj.share === share);
						if (i >= 0 && (comparison [$('#parameter2 option:selected').val()](obj.share , share) || share === '')){
	//					if (i >= 0){
						$('#div1').append('<tr>'+'<td>' + obj.firstname + '</td>' + '<td>' + obj.surname + '</td>' 
						+  '</tr>'+'<tr>'+'</tr>'
						+'<br>');
					};
							});
				
		});
		
/*	Finally I introduce another button to clear all data. You can find the code in Clear.js is self-explanatory. 

I have not included any alert message to the user in case
the outcome is empty but it could have easily been done with some code as follows:	

	if (getElementsById('div1').length === 0){
				alert (getElementsById('div1').length);
				alert ('Data are not available /for this request'); */
	 
	 });
}; 

