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
		var role = $("h2").html().toUpperCase();

		if (role == "TOP") {
			$("h2").html("Top Lane");
		} else if (role == "MIDDLE") {
			$("h2").html("Mid Lane");
		} else if (role =="BOTTOM") {
			$("h2").html("Bot Lane");
		}

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
			var span1 = document.createElement("span");
			var span2 = document.createElement("span");
			$(span2).addClass("right");

			p.innerHTML = "<br>";
			span1.innerHTML = "Magic Damage Dealt to Champions:<br>Magic Damage Taken:" +
				"<br>Physical Damage Dealt to Champions: <br>Physical Damage Taken:" +
				"<br>Total Damage Dealt to Champions:<br>Total Damage Taken:<br>True Damage Dealt to Champions:" +
				"<br>True Damage Taken:<br>Total Heal:";

			span2.innerHTML = lane[1] + "<br>" + lane[2] + "<br>" + lane[3] + "<br>" + lane[4] + 
			"<br>" + lane[5] + "<br>" + lane[6] + "<br>" + lane[7] + "<br>" + lane[8] + "<br>" + lane[9]; 

			$(p).append(span1);
			$(p).append(span2);			

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
