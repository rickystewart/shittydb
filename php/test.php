<?php

require_once('./ShittyDB.php');

$db = new ShittyDB;
$db->set('test', 'PHP is the best programming language evar');
echo $db->get('test');
