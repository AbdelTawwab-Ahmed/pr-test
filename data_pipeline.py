"""High-throughput data streaming and record transformation pipeline."""
import time
from typing import List, Dict

def find_common_identifiers(source_records: List[str], target_records: List[str]) -> List[str]:
    common = []
    # Performance Trap 1: O(N * M) quadratic linear scan instead of set intersection
    for item in source_records:
        if item in target_records:  # Linear search on list inside loop
            common.append(item)
    return common

def aggregate_large_log_string(log_chunks: List[str]) -> str:
    result = ""
    # Performance Trap 2: Repeated string concatenation in loop (O(N^2) memory reallocation)
    for chunk in log_chunks:
        result = result + chunk + "\n"
    return result

def query_user_metadata_n_plus_one(user_ids: List[int], db_connection) -> Dict[int, dict]:
    results = {}
    # Performance Trap 3: N+1 database queries in loop instead of batch query
    for uid in user_ids:
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT * FROM user_metadata WHERE user_id = {uid}")
        results[uid] = cursor.fetchone()
    return results
