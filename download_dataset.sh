OUT_DIR="dataset/fhv_hv_parquet"
mkdir -p "$OUT_DIR"

BASE_URL="https://d37ci6vzurychx.cloudfront.net/trip-data"
START_YEAR=2020
END_YEAR=2024


for YEAR in $(seq $START_YEAR $END_YEAR); do
  for MONTH in $(seq -w 1 12); do

    FILE="fhvhv_tripdata_${YEAR}-${MONTH}.parquet"
    URL="${BASE_URL}/${FILE}"
    DEST="${OUT_DIR}/${FILE}"

    if [[ -f "$DEST" ]]; then
      echo "already exists: $FILE"
      continue
    fi

    echo "downloading $FILE"

    if curl -o "$DEST" "$URL" ; then
      echo "done $FILE"
    else
      echo "not available: $FILE"
      rm -f "$DEST"
    fi

  done
done

echo "done bro, all the best for ur spark job"