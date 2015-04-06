<?php

class ShittyDB {
  public function get($key) {
    $handle = fopen($key, "r");
    $contents = fread($handle, filesize($key));
    fclose($handle);
    return $contents;
  }

  public function set($key, $value) {
    $handle = fopen($key, "w");
    $contents = fwrite($handle, $value);
    fclose($handle);
    return true;
  }
}
