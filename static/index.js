// JavaScript for homepage for Needlessly Small Rod

(function() {
	var championsNames;
	var championsIds
	var championsKeys

	$(document).ready( function() {
            trivia();
            championsNames = [];
            championsIds = [];
            championsKeys = [];
            champIcons();
            $("#selectRole").change(setRoles);  
            $("#submit").click(findBuild);       
        });

	// Pop up dialog which asks a question. If answered correctly, page loads
	// else, redirect to AP Item Changes page
	function trivia() {
		// Retrieve trivia questions
		var question = {};
		var answer = null;
		var rand = Math.floor((Math.random()*10) + 1);

		$.getJSON("trivia.json", function(data) {
			question = data["Question"+rand];
			$("#question").html(question["Question"]);
			var numsArray = ["Answer1", "Answer2", "Answer3"];
			for (var i = 3; i > 0; i--) {
				var random = Math.floor((Math.random()*i));	
				var answers = numsArray[random];
				$("#rad" + i).val(question[answers]);
				$("#answer" + i).html(question[answers]);
				$("#answer" + i).attr('for', 'rad' + i);
				numsArray.splice(random, 1);

				if (answers == "Answer3") {
					answer = question[answers];
				}
			}

		});

		$("#dialog").show();
		$("#dialog").dialog({
			autoOpen: true,
			buttons: [
				{
					text: "Submit",
					click: function() {
						var checked = $('input[name=teemo]:checked').val();
						if (checked == answer) {
							$(this).dialog("close");							
						} else {
							window.location.replace("http://nsr.lizabethd.com/apchanges/");
						}
					}
				}
			],
			closeOnEscape: false,
			dialogClass: "no-close",
			draggable: false,
			modal: true,
			hide: {
				effect: "explode",
				duration: 1000
			},
			title: "Answer Correctly to Access",
			width: 400
		});
	}

	// Retrieve JSON data of champions and on success, show the champion icons
	function champIcons() {
		$.ajax({
		    url: "champions/champs.json",
		    type: "POST",
		    dataType: "json",
	        })
		    .done(function (data) { 
		 	    showIcons(data.data); 
		})    
		    .fail(function (jqXHR, textStatus, errorThrown) { 
		    	console.log("Failed to retrieve champion data");
		});
		
	}

	// Given JSON data of champions, sort champions and their corresponding info
	// display the champion icons that can be selected
	function showIcons(data) {
		var names = [];
		var all = [];

		for(var x in data) {
			names.push(data[x].name);
			var obj = {name: data[x].name, id: data[x].id, key: data[x].key};
			all.push(obj);
		}
		names.sort();
		for (var i=0; i < names.length; i++) {
			for (var x in all) {
				if (names[i] == all[x].name) {
					championsNames.push(all[x].name);
					championsKeys.push(all[x].key);
					championsIds.push(all[x].id);
					continue;
				}
			}
		}
		for (var i=0; i < championsKeys.length; i++) {
			createImage(championsKeys[i], championsIds[i], championsNames[i]);
		}
	}

	// Create image of champion and display
	function createImage(key, id, name) {
		var image = document.createElement("img");
		$(image).attr("src", "http://ddragon.leagueoflegends.com/cdn/5.13.1/img/champion/"+key+".png");
		$(image).attr("id", id);
		$(image).attr("alt", name);
		$(image).on("click", selected);
		$("#champIcons").append(image);
	}

	// Removes any image, selected class from any and add class to clicked image
	// Also display character image on right
	function selected() {
		var index = championsNames.indexOf($(this).attr("alt"));
		var key = championsKeys[index];
		var name = championsNames[index];

		// Display character image on right
		$("#right").html("<img src='http://ddragon.leagueoflegends.com/cdn/img/champion/loading/" +
			key + "_0.jpg' alt=" + name + ">");

		// Removes all elements with the selected class
		$(".selected").removeClass("selected");

		// Add selected class to clicked element
		$(this).addClass("selected");
	}

	// Set position of marker on map based on selected role
	function setRoles() {
		var role = $(this).val();

		if (role == "Middle") {
			$("#marker").css('top', 45+"%");
			$("#marker").css('left', 40+"%");
		} else if (role == "Jungle") {
			$("#marker").css('top', 65+"%");
			$("#marker").css('left', 60+"%")
		} else if (role == "Bottom") {
			$("#marker").css('top', 80+"%");
			$("#marker").css('left', 75+"%")			
		} else {
			$("#marker").css('top', 10+"%");
			$("#marker").css('left', 10+"%")			
		}
	}

	// Check to make sure a champion was selected
	// Send selected champion and lane and redirect page to show build
	// of selected options
	function findBuild() {
		var selected = $(".selected");

		if (selected.length == 0) {
			alert("Please select a champion.");
		} else {
			var id = $(selected).attr("id");
			var name = $(selected).attr("alt");
			var key = championsKeys[championsNames.indexOf(name)];
			var role = $("#selectRole").val();

			window.location.replace("builds/index.php?id="+id+"&name="+name+
				"&key="+key+"&role="+role);
		}
	}

})();
