$('#search').change (function () {
	var player = $(this).val();
	alert('Your selected player: '+ player); 
	$(player).appendTo ('#display');
	if (this.value ==='na') return; 	
			
	$('btn1').click( function () {  
		$.getJSON (choice+'-grand-slam-winners.json', function (data){
				$.each (data.result, function (key, value) {
					var tblRowbis = '<tr>' + '<td>' + value.year + '</td>' +
					"<td>" + value.tournament + "</td>" + "<td>" + value.winner + "</td>" + "<td>" + value['runner-up'] + "</td>" + "</tr>"
						if (value.winner == player){
							$(tblRowbis).appendTo ('#userdatabis tbody')
							}
						else {$(tblRowbis).hide()
					};
			});  
		}); 
	});
});