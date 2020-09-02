		
//var doc = $.getJSON('nobel.json');
//	alert (typeof doc);

$.getJSON('nobel.json', function(data) {
    // Here, data is already an array.
//    var data_length = data.length;
//    alert (data.length);
//    for (var i = 0; i < data_length; i++) {
//        var winner = data[i]; // Here we have an object from the array
//        alert("I have an object which target is " + obj.target);
//    };

	var amount = '1';
	var path = '.prizes.laureates{.share == '+ amount + ' && .surname != \'Thaler\'}.motivation'	;	
//	var path = ".prizes.laureates{.share == \'1\' && .surname != \'Thaler\'}.motivation"	;
//	var path = '.prizes.laureates.share'
	alert (typeof path);
	alert (path);
		
    
		
	var winners = JSPath.apply(path, data);

		$('ol').append (winners);
		alert (typeof winners);

 });