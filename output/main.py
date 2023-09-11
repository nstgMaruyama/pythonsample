import nstgdb
import printf_util
import sys

if __name__ == "__main__":
  pri = printf_util.Printf_Util()
  pri.log_level = 4
  pri_ = pri.printf
  database = nstgdb.Nstgdb(printf_func = pri_)
  database.nstgdb_run(sys.argv[1])