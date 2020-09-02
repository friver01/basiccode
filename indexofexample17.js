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



// I introduce this variable to facilitate the conversion from a string
// (the values I get from the comparison dropdown list that is selected by 
// the user into a javascript comparison operator

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

function retrieve() { 
	$.getJSON('nobel.json', function(data) {
		// Here, data is already an array.
	//    var data_length = data.length;
	//    alert (data.length);
	//    for (var i = 0; i < data_length; i++) {
	//        var winner = data[i]; // Here we have an object from the array
	//        alert("I have an object which target is " + obj.target);
	//    };
		var share = $('#share option:selected').text();
		var category = $('#categories option:selected').text();
		var year = document.getElementById("addressYear").value;
		var compare = document.getElementById("surname").value;
		var parameteryearsel = document.getElementById("parameter1").value;
		var parametersharesel = document.getElementById("parameter2").value;
		alert (typeof parametersharesel);
		alert (parametersharesel);
		var path = '.prizes{.year'+ parameteryearsel+ '\''+year+'\' &&.category *=\''+category
		+'\'  &&..surname *= \''+compare+'\'&&..share'+ parametersharesel+ ' \''+share+'\'}';	
	//	var path = '.prizes.laureates{.surname *= \'Curie\'}'	;
	//	var path = '.prizes.laureates{.share == '+ amount + '}'	;	
	//	var path = ".prizes.laureates{.share == \'1\' && .surname != \'Thaler\'}.motivation"	;
	//	var path = '.prizes.laureates.share'
		alert (typeof path);
		alert (path);
		var comparison = {
			'*=': function (x, y) { return x === y },
			'>=': function (x, y) { return x >= y },
			'<=': function (x, y) { return x <= y }
				};
			
		var winners = JSPath.apply(path, data);

	//		$('ol').append (winners);
	//		alert (typeof winners);
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
	//		$.each (value.laureates, function (key, obj) {
	//		$('ol').append('<tr>' + '<td>' + obj.firstname + '</td>' +
	//					"<td>" + obj.surname + '<td>' + obj.share + '</td>' + "</tr>");
	//		});					
		});
//			if (getElementsById('div1').length === 0){
//				alert (getElementsById('div1').length);
//				alert ('Data are not available /for this request');
//		 }
	 
	 });
}; 

//$('clear').click( function () { 
//	$('#div2').empty();
//	$('#div1').empty();


// });