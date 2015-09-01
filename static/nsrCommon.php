<!-- PHP common page for Needlessly Small Rod -->

<?php
	function side_nav() {
?>
		<div class="col-md-3">
			<ul class="nav nav-pills nav-stacked">
		    	<li class="active"><a id="home" href="/">Home</a></li>
			    <li><a id="changes" href="/apchanges">AP Item Changes</a></li>
		    	<li class="dropdown">
		      		<a id="about" class="dropdown-toggle" data-toggle="dropdown" href="#">About<span class="caret"></span></a>
			      	<ul class="dropdown-menu">
			        	<li><a href="/documentation">Documentation</a></li>
			        	<li><a href="https://developer.riotgames.com/discussion/announcements/show/2lxEyIcE">Riot API Competition 2.0</a></li>                       
			      	</ul>
		    	</li>			    
			</ul>
		</div>
<?php
	}

	function footer() {
	?>
		<footer>
			August 31, 2015.
			<br>
			Riot Games and League of Legends are registered trademarks of Riot Games, Inc. League of Legends 
			© Riot Games, Inc. 
			<br>
			Lizabethd.com and Needlessly Small Rod are not endorsed by Riot Games or League 
			of Legends in any way.</p>
		</footer>
	<?php
	}
?>