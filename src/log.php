<?php 
$target_dir = "log/";

print_r($_FILES);
echo count($_FILES)."files uploaded";
foreach($_FILES as $key=>$val){
    $target=$target_dir.basename($_FILES[$key]["name"]);
    
    $fileType=strtolower( substr($target, -3) );
    echo $fileType;
    $uploadOk=1;    
    // Check file size
    if ($_FILES[$key]["size"] > 500000) {
        echo "Sorry, your file is too large.";
        $uploadOk = 0;
    }

    // Allow certain file formats
    if($fileType != "txt" && $fileType != "dat" && $fileType != ".db" ) {
    echo "Sorry, only .txt, .dat, files are allowed. your file was :".$fileType;
    $uploadOk = 0;
    }

    // Check if $uploadOk is set to 0 by an error
    if ($uploadOk == 0) {
        echo "Sorry, your file was not uploaded.";
    // if everything is ok, try to upload file
    } else {
        echo"trying t upload\n";
        if (move_uploaded_file($_FILES[$key]["tmp_name"], $target)) {
        echo "The file ". htmlspecialchars( basename( $_FILES[$key]["name"])). " has been uploaded.";
        } else {
        echo "Sorry, there was an error uploading your file.";
        }
    }
}