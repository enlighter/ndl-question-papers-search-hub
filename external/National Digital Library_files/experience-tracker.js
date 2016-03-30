function logStatement(object, id) {
	$.post("../../ajax/exp_track/user_experience_tracker.php", {
		obj : JSON.stringify(object),
		flag : id,
	}, function(reply, status) {
			//console.log(reply);
	});
}
