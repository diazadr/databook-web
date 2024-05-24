from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi
from datetime import datetime


MONGO_URI = "mongodb+srv://diazadriansyah1933:eSfXInPGcBHl8vlI@cluster0.iskhk7c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "buku_db"

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB setup
client = MongoClient(MONGO_URI, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)
db = client[DATABASE_NAME]
buku_collection = db['buku']
penerbit_collection = db['penerbit']
penulis_collection = db['penulis']
kota_collection = db['kota']

app.route('/')
def index():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return "Pinged your deployment. You successfully connected to MongoDB!"
    except Exception as e:
        print("Error:", e)
        return "Failed to connect to MongoDB! Error: " + str(e)

@app.route('/')
def index():
    return render_template('buku/list_buku.html')

#BUKU
@app.route('/buku', methods=['GET', 'POST'])
def input_buku():
    if request.method == 'POST':
        judul = request.form['judul_buku']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']
        tahun_terbit = request.form['tahun_terbit']
        kota = request.form['kota']
        sinopsis = request.form['sinopsis']
        jumlah_halaman = request.form['jumlah_halaman']

        buku_data = {
            'judul': judul,
            'penulis': penulis,
            'penerbit': penerbit,
            'tahun_terbit': tahun_terbit,
            'kota': kota,
            'sinopsis': sinopsis,
            'jumlah_halaman': jumlah_halaman
        }

        buku_collection.insert_one(buku_data)
        flash('Data buku berhasil ditambahkan.', 'success')
        return redirect(url_for('list_buku'))

    # Ambil data penulis, penerbit, dan kota dari database
    penulis_list = penulis_collection.find()
    penerbit_list = penerbit_collection.find()
    kota_list = kota_collection.find()

    return render_template('buku/buku.html', penulis_list=penulis_list, penerbit_list=penerbit_list, kota_list=kota_list)


@app.route('/buku/list', methods=['GET'])
def list_buku():
    buku_list = buku_collection.find()
    return render_template('buku/list_buku.html', buku_list=buku_list)

@app.route('/buku/edit/<id>', methods=['GET', 'POST'])
def edit_buku(id):
    buku = buku_collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        judul = request.form['judul']
        penulis = request.form['penulis']
        penerbit = request.form['penerbit']
        tahun_terbit = request.form['tahun_terbit']
        kota = request.form['kota']
        sinopsis = request.form['sinopsis']
        jumlah_halaman = request.form['jumlah_halaman']

        buku_collection.update_one({'_id': ObjectId(id)}, {'$set': {
            'judul': judul,
            'penulis': penulis,
            'penerbit': penerbit,
            'tahun_terbit': tahun_terbit,
            'kota': kota,
            'sinopsis': sinopsis,
            'jumlah_halaman': jumlah_halaman
        }})
        flash('Data buku berhasil diperbarui.', 'success')
        return redirect(url_for('list_buku'))

    penulis_list = penulis_collection.find()
    penerbit_list = penerbit_collection.find()
    kota_list = kota_collection.find()

    return render_template('buku/edit_buku.html', buku=buku, penulis_list=penulis_list, penerbit_list=penerbit_list, kota_list=kota_list)

@app.route('/buku/delete/<id>')
def delete_buku(id):
    buku_collection.delete_one({'_id': ObjectId(id)})
    flash('Data buku berhasil dihapus.', 'success')
    return redirect(url_for('list_buku'))

# PENERBIT
@app.route('/penerbit', methods=['GET', 'POST']) 
def penerbit():
    if request.method == 'POST':
        nama_penerbit = request.form['nama_penerbit'] 
        data = {
            'nama_penerbit': nama_penerbit
        }
        penerbit_collection.insert_one(data)
        return redirect('/list_penerbit')
    return render_template('penerbit/penerbit.html')

@app.route('/list_penerbit', methods=['GET'])
def list_penerbit():
    list_penerbit = penerbit_collection.find()
    return render_template('penerbit/list_penerbit.html', penerbit=list_penerbit)

@app.route('/edit_penerbit/<id>', methods=['GET', 'POST'])
def edit_penerbit(id):
    penerbit = penerbit_collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        nama_penerbit = request.form['nama_penerbit']
        penerbit_collection.update_one({'_id': ObjectId(id)}, {'$set': {'nama_penerbit': nama_penerbit}})
        return redirect('/list_penerbit')  # Perbaikan di sini, gunakan path URL '/list_penerbit'
    return render_template('penerbit/edit_penerbit.html', penerbit=penerbit)


@app.route('/delete_penerbit/<id>')
def delete_penerbit(id):
    penerbit_collection.delete_one({'_id': ObjectId(id)})
    return redirect('/list_penerbit')

# PENULIS
@app.route('/penulis', methods=['GET', 'POST'])
def penulis():
    if request.method == 'POST':
        nama_penulis = request.form['nama_penulis']
        data = {
            'nama_penulis': nama_penulis
        }
        penulis_collection.insert_one(data)
        flash('Data penulis berhasil ditambahkan.', 'success')
        return redirect('/list_penulis')
    return render_template('penulis/penulis.html')

@app.route('/list_penulis')
def list_penulis():
    list_penulis = penulis_collection.find()
    return render_template('penulis/list_penulis.html', penulis=list_penulis)


@app.route('/edit_penulis/<id>', methods=['GET', 'POST'])
def edit_penulis(id):
    penulis = penulis_collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        nama_penulis = request.form['nama_penulis']
        penulis_collection.update_one({'_id': ObjectId(id)}, {'$set': {'nama_penulis': nama_penulis}})
        flash('Data penulis berhasil diperbarui.', 'success')
        return redirect(url_for('list_penulis'))
    return render_template('penulis/edit_penulis.html', penulis=penulis)

@app.route('/hapus_penulis/<id>')
def hapus_penulis(id):
    penulis_collection.delete_one({'_id': ObjectId(id)})
    flash('Data penulis berhasil dihapus.', 'success')
    return redirect(url_for('list_penulis'))

# KOTA
@app.route('/kota', methods=['GET', 'POST']) 
def kota():
    if request.method == 'POST':
        nama_kota = request.form['nama_kota'] 
        data = {
            'nama_kota': nama_kota
            }
        kota_collection.insert_one(data)
        return redirect('/list_kota')
    return render_template('kota/kota.html')

@app.route('/list_kota', methods=['GET'])
def list_kota():
    list_kota = kota_collection.find()
    return render_template('kota/list_kota.html', kota=list_kota)

@app.route('/edit_kota/<id>', methods=['GET', 'POST'])
def edit_kota(id):
    kota = kota_collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        nama_kota = request.form['nama_kota']
        kota_collection.update_one({'_id': ObjectId(id)}, {'$set': {'nama_kota': nama_kota}})
        flash('Data kota berhasil diperbarui', 'success')
        return redirect('/list_kota')
    return render_template('kota/edit_kota.html', kota=kota)

@app.route('/delete_kota/<id>')
def delete_kota(id):
    kota_collection.delete_one({'_id': ObjectId(id)})
    flash('Data kota berhasil dihapus', 'success')
    return redirect('kota/list_kota')

if __name__ == '__main__':
    app.run(debug=True)