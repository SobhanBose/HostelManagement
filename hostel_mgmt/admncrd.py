import pickle

f_in = open("pvt.dat", "wb")

# password = "admin123"

pickle.dump("admin123", f_in)

f_in.close()