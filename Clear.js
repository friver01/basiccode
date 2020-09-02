function clear () {
	$('#div2').empty();
	$('#div1').empty();
	$('#addressYear').prop('selectedIndex',0); 
	$('#share').prop('selectedIndex',0);
	$('#categories').prop('selectedIndex',0);
	$('#parameter1').prop('selectedIndex',0');
	$('#parameter2').prop('selectedIndex',0');
};

Clear.addEventListener("click", clear);