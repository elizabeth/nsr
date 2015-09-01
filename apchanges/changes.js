(function() {
	var apItems;
	var items;

	$(document).ready( function() {
		apItems = {};
		items = {};
		itemsJson();
	});

	function itemsJson() {
		$.getJSON("../items/apItems.json", function(apData) {
			apItems = apData;

			$.getJSON("../items/items.json", function(data) {
				items = data.data;
				images();
			});
		});	
	}

	function images() {
		for(var x in apItems) {
			image(apItems[x].name, apItems[x].id);
		}
	}

	function image(name, img_id) {
		var pic_id = getId(name);	

		$("#"+img_id).attr("src", "http://ddragon.leagueoflegends.com/cdn/5.14.1/img/item/" + pic_id + ".png");
	} 

	function getId(name) {
		for(var x in items) {
			if (items[x].name == name) {
				return items[x].id
			}
		}
		return 1058;		
	}
})();


