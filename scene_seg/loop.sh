input="last.txt"
echo "hello"
while IFS= read -r line
do
  echo "hello"
  echo "$line"
  srun --gres=gpu:1 python -u train_scene_seg_s3dis.py "$line"
done < "$input"
