#Moves files from projec folder  to git repo folder


$home_path = "D:\projects"
$migration_path = "D:\computer_science_icstars"

function migrate-files ($home_path, $migration_path) {
    if((test-path $home_path) -and (test-path $migration_path)){
        copy-item -Path $home_path -Destination $migration_path -Recurse -Force
    }

}