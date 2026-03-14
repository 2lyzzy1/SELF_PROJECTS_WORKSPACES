<?php
echo "Come back here.\n";
$a = 5; $b = 10; $c = $a + $b;
?>
<?php if ($c!=15): ?>
    <p> <?php echo $c; ?> </p>
<?php endif; ?>
<?php echo "Good" ?>
