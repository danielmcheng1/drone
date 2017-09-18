thisname=stitch.sh
mission=$1
ydm=$2
hms=$3

output_base_dir=/home/danielmcheng1/drone/static/images
raw_base_dir=/home/danielmcheng1/android
raw_sub_dir=$1/$2/$3

output_full_dir=$output_base_dir/$raw_sub_dir
raw_full_dir=$raw_base_dir/$raw_sub_dir
raw_num_files=`ls -1 $raw_full_dir | wc -l`


echo "$thisname: Raw directory is $raw_full_dir"
echo "$thisname: Output directory is $output_full_dir"

# make the output subfolder first (if not already existing)
echo "$thisname: Creating output folder"
mkdir -p $output_full_dir

# copy over a backup in case stitching fails (or in case we don't want to stitch)
# this copies the first file by timestamp 
echo "$thisname: Creating backup based on first image"
cp -p $raw_full_dir/`ls $raw_full_dir | head -n 1` $output_full_dir/backup.jpeg


# run hugin stitch if we have more than 1 file 
if [[ "$raw_num_files" -eq 1 ]];
then
  echo "$thisname: Did not run stitching because only one file was found in raw directory"
else
  echo "$thisname: Starting to stitch now"
  exit 1
  pto_gen --output $output_full_dir/mission.pto --fov 50 $raw_full_dir/*
  hugin_executor --assistant $output_full_dir/mission.pto
  hugin_executor --stitching --prefix $output_full_dir/stitched $output_full_dir/mission.pto
fi
