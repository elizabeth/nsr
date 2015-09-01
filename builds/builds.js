// JavaScript for builds page for Needlessly Small Rod

(function() {
	$(document).ready( function() {
    	builds();   

    	$("#rankedButton").click(displayRanked);
    });

	// Get and display the best builds 
	function builds() {
		var beforeBuilds = {};
		var id = $("#right img").attr("id");
		var role = $("h3").html().replace(' Lane', '').toUpperCase();

		// Get before normal builds
		getBuild("na5.11NormBuilds.json", id, role, "beforeNorms");

		// Get after normal builds
		getBuild("na5.14NormBuilds.json", id, role, "afterNorms");

		// Get before rank builds
		getBuild("na5.11RankBuilds.json", id, role, "beforeRanked");

		// Get after rank builds
		getBuild("na5.14RankBuilds.json", id, role, "afterRanked");
	}

	// Gets and displays build and stats for given champion
	function getBuild(file, id, role, div_id) {
		$.getJSON("/../stats/bestBuilds/" + file, function(data) {
			var lane = data[id].lane[role].build;
			for (var i = 0; i < lane[0].length; i++) {
				var pic = lane[0][i];
				if (pic != 0) {
					var image = document.createElement("img");
					$(image).attr("src", "http://ddragon.leagueoflegends.com/cdn/5.14.1/img/item/"+pic+".png");
					$("#"+div_id).append(image);
				}
			}
			var p = document.createElement("p");
			p.innerHTML = "<br>Magic Damage Dealt to Champions: " +
			lane[1] + "<br>Magic Damage Taken: " + lane[2] +
			"<br>Physical Damage Dealt to Champions: " + lane[3] +
			"<br>Physical Damage Taken: " + lane[4] + "<br>Total Damage Dealt to Champions: " +
			lane[5] + "<br>Total Damage Taken: " + lane[6] + "<br>True Damage Dealt to Champions: " +
			lane[7] + "<br>True Damage Taken: " + lane[8] + "<br>Total Heal: " + lane[9];
			
			$("#"+div_id).append(p);			
		});
	}

		// Displays either ranked or normal builds and stats
	function displayRanked() {
		if ($("#rankedButton").html() == "View Ranked") {
			$("#rankedButton").html("View Normal");	
		} else {
			$("#rankedButton").html("View Ranked");			
		}
		$("#norms").toggle();
		$("#ranked").toggle();
	}

})();
