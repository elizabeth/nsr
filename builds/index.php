<!DOCTYPE html>
<html>
	<!-- 
		Builds Page for Needlessly Small Rod
	-->
	<head>
		<meta charset="utf-8" />
		<title>Builds - NSR</title>

		<!-- Twitter Bootstrap -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
 		<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>		

 		<!-- jQuery -->
 		<link rel="stylesheet" href="http://code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
		<script src="http://code.jquery.com/jquery-1.10.2.js"></script>
		<script src="http://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>


 		<link href="../static/styles.css" type="text/css" rel="stylesheet" />		
 		<link href="builds.css" type="text/css" rel="stylesheet" />

		<script language="javascript" type="text/javascript" src="builds.js"></script>
 		
		<link href="http://ddragon.leagueoflegends.com/cdn/5.2.1/img/profileicon/642.png" type="image/png" rel="shortcut icon" />
	</head>

	<body>
		<div id="wrapper">
			<?php 
				$id = $_GET["id"];
				$name = $_GET["name"];
				$key = $_GET["key"];
				$role = $_GET["role"];
			?>

			<?php include '../static/nsrCommon.php'; ?>
			
			<?php side_nav(); ?>
			
			<div id="main">
				<h1><?=$name?></h1>
				<h3><?= $role ?> Lane</h3>

				<p id="sum">Builds and stats before and after AP item changes of Patch 5.13.
					<button id="rankedButton" type="button" class="btn btn-default">View Ranked</button>
				</p>

				<div id="norms" class="build">
				Normals<br>
					<div id="beforeNorms">Before:<br></div>				
					<div id="afterNorms">After:<br></div>				
				</div>

				<div id="ranked" class="build">
				Ranked<br>
					<div id="beforeRanked">Before:<br></div>
					<div id="afterRanked">After:<br></div>
				</div>

	        	<div id="right"><img id=<?= $id?>
					src='http://ddragon.leagueoflegends.com/cdn/img/champion/loading/<?=$key?>_0.jpg'
					alt=<?= $name ?>></div>
			</div>

			<div id="bottom">
				<br><br>
				<?php footer(); ?>
			</div>
		</div>	
	</body>
</html>
