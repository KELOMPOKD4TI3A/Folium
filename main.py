#!/bin/python

import folium

def surabaya1(selalu,terbaik):
	bocahmicin = folium.Map(
    location=[selalu,terbaik],
    zoom_start=12,
    tiles='Stamen Terrain')
	return bocahmicin

def surabaya2(selalu1,terbaik1):
	micin = folium.Map(
    location=[selalu1,terbaik1],
    zoom_start=12,
    tiles='Stamen Terrain')	
	return micin

def surabaya3(selalu2,terbaik2):
	bocah = folium.Map(
	location=[selalu2,terbaik2],
	zoom_start=12,
    tiles='Stamen Terrain')	
	return bocah
	
def simpan(banyak,sekali):
	banyak.save(sekali)
	
bocahmicin 	= surabaya1(-7.3044144,112.7412095)
micin		= surabaya2(-7.3044144,112.7412095)
bocah		= surabaya3(-7.3044144,112.7412095)

folium.Marker(
    location=[-7.296218, 112.738667],
    popup='Surabaya Zoo',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.265440, 112.750301],
    popup='Monumem Kapal Selam Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.264820, 112.750417],
    popup='Moncafe (Monkasel Caffe)',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.263952, 112.750346],
    popup='Skate Park Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.262582, 112.748980],
    popup='Sekolah Nasional Tiga Bahasa Little Sun School',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.262865, 112.748857],
    popup='Sasana Wushu YASANIS',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.264150, 112.749183],
    popup='Embassy English Centre',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.268390, 112.747916],
    popup='KPP Pratama Surabaya Genteng',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.268040, 112.747812],
    popup='The WIN Hotel Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.268312, 112.747679],
    popup='Masjid An Nur (Kantor Pajak)',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.258340, 112.751175],
    popup='Kampoeng Stik',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.257855, 112.751642],
    popup='Sachman Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.257309, 112.749175],
    popup='Sekolah Menengah Atas Negeri 1 Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.257005, 112.749230],
    popup='Sekolah Menengah Atas Negeri 2 Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.257387, 112.748216],
    popup='Kantor Bappeko Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.257807, 112.747708],
    popup='Dinas Kominfo Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.257893, 112.748220],
    popup='Masjid Al Muhajirin',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.257302, 112.746237],
    popup='Hotel Royal Regal Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.258302, 112.748605],
    popup='My Grill Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.259627, 112.746969],
    popup='Kantor Walikota Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)


folium.Marker(
    location=[-7.229636, 112.766269],
    popup='Sidotopo Wetan',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.280613, 112.770057],
    popup='KFC Manyar',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.279612, 112.766720],
    popup='Pizza Hut Manyar',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.277314, 112.766087],
    popup='Boncafe Manyar',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.280176, 112.768930],
    popup='Ayam Bakar Primarasa',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.278272, 112.766549],
    popup='Ikan Bakar Cianjur',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.278921, 112.765476],
    popup='Bonet Supermarket',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.280113, 112.766120],
    popup='Hakata Ikkousha',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.279868, 112.764027],
    popup='Gramedia Manyar',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.280102, 112.772460],
    popup='BCA KCP Kertajaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.313033, 112.728353],
    popup='Bank BTN',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.312661, 112.727430],
    popup='Gedung GEMA UNESA',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.311842, 112.726593],
    popup='Pascasarjana Unesa',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.314024, 112.727618],
    popup='Lapangan UNESA',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.314168, 112.726180],
    popup='RanUnesa',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.314370, 112.726754],
    popup='Kafe Unesa',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.314583, 112.727419],
    popup='UNESA Library',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.314748, 112.728095],
    popup='Pusat Bahasa Universitas Negeri Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.313785, 112.725343],
    popup='Masjid Unesa Ketintang',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.315482, 112.724560],
    popup='Unesa University Press',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.315812, 112.724372],
    popup='Lembaga Penjaminan Mutu Pendidikan (LPMP) Jawa Timur',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.316047, 112.748636],
    popup='Plasa Marina Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.316003, 112.748831],
    popup='Adira',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.315823, 112.748923],
    popup='Axioo',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.316344, 112.748537],
    popup='Galeri Indosat Plaza Marina',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.316738, 112.748698],
    popup='BII ATM Sinar Fontana Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.316344, 112.748210],
    popup='McDonalds',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.315937, 112.748605],
    popup='HokBen Plasa Marina',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.316298, 112.748005],
    popup='Samsung Partner Plaza - PEACE CELL - PLASA MARINA',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.316024, 112.749291],
    popup='Parkir Timur Plaza Marina',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.315294, 112.748474],
    popup='Apartemen Puncak Marina Tower 1',
    icon=folium.Icon(color='blue')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.222785, 112.735106],
    popup='Tokoraket.com',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.220992, 112.732998 ],
    popup='Perak Photo',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.221663, 112.731764 ],
    popup='PT. Pelayaran Meratus',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.218842, 112.730257 ],
    popup='GAMA-Group',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.215881, 112.729800 ],
    popup='Sami Jaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.214343, 112.728389 ],
    popup='Toko Abrilia',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.213327, 112.727268 ],
    popup='Yonif 1 Marinir',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.210098, 112.723294 ],
    popup='Cumi Hitam 19',
   icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.210042, 112.722781 ],
    popup='Pelni Surya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.206868, 112.721786 ],
    popup='PT. Petro Andalan Nusantara',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.198897, 112.731820],
    popup='Terminal Jamrud',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)


folium.Marker(
    location=[-7.311603, 112.795602],
    popup='Bakso Cak Dul',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.311664, 112.795814],
    popup='Warkop Pak Salem',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.311310, 112.796128],
    popup='Mie Ayam & Ceker Pak Men',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.311185, 112.795961],
    popup='Aifa Palapa',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.311677, 112.796321],
    popup='Family Telur',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.311877, 112.796691],
    popup='Warkop Karambol',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.311688, 112.797128],
    popup='Bakso Cak Heru',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.311254, 112.797126],
    popup='Pentol Tuna',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.311568, 112.795379],
    popup='Iwan Elektronik',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.311558, 112.795186],
    popup='Zahara Elektronik',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

bocahmicin

folium.Marker(
    location=[-7.195429, 112.739471 ],
    popup='Monumen Jalesveva Jayambe',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.196121, 112.742958  ],
    popup='KRI Dewa Ruci',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.195361, 112.743256 ],
    popup='Gd. PTA',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.195426, 112.744312 ],
    popup='Diskomlekal Koarmatim',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.194862, 112.745514 ],
    popup='Bengkel Fasharkan Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.197573, 112.743774  ],
    popup='E Wharf',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.196988, 112.731659 ],
    popup='KopiLot Surabaya ',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.198126, 112.732229 ],
    popup='PT. Pelindo 3',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.196694, 112.732723 ],
    popup='Food Court SNQ',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.196721, 112.733404 ],
    popup='The Markonah Resto & Bar',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.224919, 112.787856],
    popup='Air Mancur Taman Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.224797, 112.787975],
    popup='Warkop81',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.223414, 112.787488],
    popup='Markas SDW Group',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.222840, 112.787331],
    popup='Mushola Hikudritolilah',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.222187, 112.787522],
    popup='TAMAN PENDIDIKAN AL-QURAN DARUL FALACH',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.221971, 112.787402],
    popup='Warung Cak Munir',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.221455, 112.787368],
    popup='Zubaidah Borneo Fried Chiken',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.220610, 112.787384],
    popup='Masjid Al - Mabrur',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.220558, 112.787164],
    popup='Madrasah Ibtidaiyah Ribath Darut Tauhid',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.220796, 112.786961],
    popup='warkop GTT',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.256237, 112.751363],
    popup='Kelurahan Ketabang',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.258765, 112.750797],
    popup='PT Mastrada Surya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.256224, 112.752060],
    popup='GBI Ambengan',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.258337, 112.747794],
    popup='Yayasan Kas Pembangunan',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.257641, 112.747492],
    popup='Kantor Pemerintah Kota Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.258379, 112.748569],
    popup='Asoka',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.255759, 112.748879],
    popup='Princess Photo Studio Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.253498, 112.750316],
    popup='Taman Remaja Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.252583, 112.749436],
    popup='Apotik Kusuma',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.256744, 112.750813],
    popup='Ganesha Operation',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.219674, 112.713401],
    popup='Armada Timur TNI AL Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.221199, 112.719029],
    popup='Pudislek Bomimoro Kodingkal Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.221477, 112.719500],
    popup='SMK Khusus Angkatan Laut',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.221748, 112.717042],
    popup='Lemabaga Pendidikan TNI AL',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.213781, 112.720752],
    popup='PT Terminal Petikemas Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.214228, 112.7234337],
    popup='Cahaya Berkah Abdi',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.214682, 112.724296],
    popup='PT Intiboga Sejahtera',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.214741, 112.724771],
    popup='Bahana Line',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.213002, 112.725659],
    popup='Mako Lantamal V Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.212116, 112.724490],
    popup='RSAL Tanjung Perak',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.282336, 112.792975],
    popup='Masjid Manarul Ilmi',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.283773, 112.791907],
    popup='GOR Futsal Pertamina ITS',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.281198, 112.794049],
    popup='Departemen Arsitektur ITS',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.282245, 112.795090],
    popup='Institut Teknologi Sepuluh Nopember',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.281395, 112.794575],
    popup='Rektorat ITS',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.284961, 112.794983],
    popup='Departemen Matematika ITS',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.285142, 112.796533],
    popup='Teknik Elektro ITS',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.285185, 112.797375],
    popup='Fakultas Teknologi Industri',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.286727, 112.793073],
    popup='Gelanggang Olah Raga (GOR) Bulutangkis ITS',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.277458, 112.795841],
    popup='Politeknik Perkapalan Negeri Surabaya (PPNS)',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.344749, 112.795751],
    popup='Balai Pelatihan Dan Pendidikan Ilmu Pelayaran (BP2IP) Surabaya - Kampus II',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.345292, 112.793083],
    popup='Konveksi Surabaya Griya rasukan',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.344618, 112.796784],
    popup='Cak Syam Barbershop',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.346590, 112.797199],
    popup='Perumahan Citra Candra Asri',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.346417, 112.798886],
    popup='Perum The Amerta Green Land',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.345810, 112.799444],
    popup='Amega Crown Residence',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.345113, 112.801226],
    popup='PT. Lastindo Jaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.346193, 112.802717],
    popup='Masjid Tambakoso',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.346778, 112.803084],
    popup='Lembaga Pendidikan Ma Ariel Madrasah Ibtidaiyah Darul Ulum',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.346604, 112.803524],
    popup='Kampung batik sda',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.263560, 112.748326],
    popup='Surabaya Suites Hotel',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.263528, 112.748190],
    popup='ATM Bank Permata Plaza Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.261356, 112.748162],
    popup='Sanyo Fisher',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.261385, 112.748824],
    popup='TIKET SURABAYA ONLINE',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.260492, 112.749805],
    popup='Nurul Fikri',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.260220, 112.749441],
    popup='Jonas Photo',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.245781, 112.751162],
    popup='Kantor Pos Surabaya Ketabang',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.245890, 112.751209],
    popup='Spesial Ceker Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.261675, 112.750365],
    popup='Golds Gym Grand City Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.260999, 112.739572],
    popup='Monumen Pers Perjuangan Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.204424, 112.763150],
    popup='Warkop Pojokan',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.204902, 112.763287],
    popup='Bandeng Presto BU ROHANAH',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.204759, 112.764352],
    popup='Kios & Warnet Ammar',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.205376, 112.763016],
    popup='Presto Ibu Umi Kalsum',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.205280, 112.763480],
    popup='Masjid Rayadthus Sholihin',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.205043, 112.764413],
    popup='Warung Suyoggg',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.205070, 112.764515],
    popup='"Warkop Suyog"',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.205642, 112.762851],
    popup='Warung Giras Cak Ayik',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.205878, 112.763458],
    popup='Warung Klepas',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.205954, 112.764025],
    popup='Kedai Kopi Klepas Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.196846, 112.732435],
    popup='Surabaya North Quay',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.198201, 112.733421],
    popup='PT Pelabuhan Indonesia III',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.199721, 112.734013],
    popup='Polresta Tanjung Perak',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.201121, 112.732647],
    popup='PT Dok Dan Perkapalan Surabaya ',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.201874, 112.733512],
    popup='Sepinggan Indah Travel',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.202882, 112.733801],
    popup='PT Dharma Lautan Utama',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.201388, 112.733458],
    popup='Kantor Kesehatan Pelabuhan (KKP) Kelas I Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.203829, 112.733872],
    popup='KPPBC Tipe Madya Pabean Tanjung Perak',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.203769, 112.733257],
    popup='PGN SAKA',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.204349, 112.733265],
    popup='Kementerian Perhubungan Direktorat Jenderal Perhubungan Laut Distrik Navigasi Kelas I Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.228524, 112.722189],
    popup='TAMAN TANJUNG SADARI',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.228393, 112.721719],
    popup='Garasi Trailler',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.228967, 112.722944],
    popup='Masjid Al Muttaqiin',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.228896, 112.723550],
    popup='Celebes Surabaya Transport. PT',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.228341, 112.722775],
    popup='Waroeng Sunda',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.228633, 112.722731],
    popup='CV. ALBA TRANS',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.228573, 112.723655],
    popup='MotoGPLand',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.227973, 112.723194],
    popup='Indoline Incomekita. PT',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.229888, 112.722665],
    popup='Sekolah Menengah Atas Hang Tuah - 1 Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.230288, 112.721459],
    popup='Persewaan Mobil Sumber Barokkah',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.231825, 112.719007],
    popup='Warung Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.232005, 112.719127],
    popup='Warung Pojok',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.231732, 112.718867],
    popup='Masjid Taqwirayul',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.231245, 112.716621],
    popup='Warung Imbok',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.231418, 112.717517],
    popup='Al Manar Herbafit Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.231450, 112.717339],
    popup='Toko Hera',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.231619, 112.717144],
    popup='Toko Sekar Jaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.231492, 112.717794],
    popup='Anugerah',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.231228, 112.715628],
    popup='Vista',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.230742, 112.715048],
    popup='GPS',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.373915, 112.779746],
    popup='DPPU Juanda Pertamina Aviation',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.374607, 112.782013],
    popup='Taman Alat Stasiun Meteorologi Juanda Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.374330, 112.783955],
    popup='PT. Suryagita Nusaraya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.374905, 112.783258],
    popup='ATT Cargo',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.374884, 112.784084],
    popup='Terminal Kargo Juanda T1',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.374437, 112.784878],
    popup='DHL Express SUB',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.376129, 112.786348],
    popup='Fire Station Bandar Udara Juanda',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.374033, 112.787990],
    popup='Angkasa Pura Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.373452, 112.793790],
    popup='Parkir Domestik',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.374005, 112.796011],
    popup='Parkir International',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.197900, 112.734440],
    popup='Indonesia Ferry Asdp',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.198086, 112.734751],
    popup='Terminal ferry Tanjung Perak, Tanjung Perak Barat',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.198451, 112.734826],
    popup='Pelabuhan Perak Madura',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.197820, 112.732766],
    popup='ATM Bank Jatim',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.198247, 112.733305],
    popup='BNI PELINDO III',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.198302, 112.732972],
    popup='Serikat Pekerja PT Pelindo III',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.198757, 112.733754],
    popup='Masjid Baitul Hakam Pelabuhan Tanjung Perak Surabaya',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.198986, 112.734144],
    popup='Dobek Rumah Makan',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.199827, 112.732962],
    popup='Pos Jamrud',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.200034, 112.733545],
    popup='Rumah Makan Aroma Makassar',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.199094, 112.734905],
    popup='Divisi Terminal Kalimas',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.198959, 112.733653],
    popup='OMI SILVER MART',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.199578, 112.734068],
    popup='Polsekta KP3 Tanjung Perak',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.200462, 112.733100],
    popup='Widasari Prima',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.200365, 112.733261],
    popup='Toko Gading Murni',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.200305, 112.733413],
    popup='Gading Murni Perak',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.199754, 112.733998],
    popup='Polresta Tanjung Perak',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.200198, 112.733676],
    popup='Tk.Ainy',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.200030, 112.734040],
    popup='PT. Citrabuana Indoloka',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.200074, 112.734243],
    popup='Perusahaan Pelayaran Inti Irama Lines',
    icon=folium.Icon(icon='cloud')
).add_to(bocahmicin)

bocahmicin


folium.Marker(
	location=[-7.289308, 112.764022],
    popup='Tuban Raya',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
    location=[-7.232236, 112.720168],
    popup='SPBU Pertamina 54.601.19',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.232836, 112.721022],
    popup='Hotel Antariksa',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.233659, 112.721274],
    popup='Klenteng Mbah Ratu',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.233757, 112.720880],
    popup='Graha SBI',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.233935, 112.720876],
    popup='Kursus Bahasa Jerman Surabaya',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.233295, 112.720266],
    popup='Boezem Morokrembangan',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.234261, 112.720828],
    popup='PT. Baraka Sarana Tama',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.234616, 112.721002],
    popup='Nasi Tempe Penyet Pak Hambali',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.235149, 112.720446],
    popup='Tunas Jaya. CV',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.235376, 112.720588],
    popup='Warung Nasi Pecel Intisari',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.276103, 112.707406],
    popup='FIF GROUP Surabaya 3',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.276073, 112.707261],
    popup='Djoeragan Sego',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.276059, 112.707119],
    popup='Toko Buku Kwan',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.276014, 112.707549],
    popup='FIF Kupang Jaya',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.275563, 112.708146],
    popup='Kebab Marlin',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.275730, 112.707404],
    popup='Pertamina',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.276321, 112.707480],
    popup='Babyceloshop',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.276502, 112.707993],
    popup='Penyetan bang ali',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.277759, 112.708022],
    popup='Pat Bing Soo',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.277592, 112.707991],
    popup='Rumah Pantai Eatery',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.269771, 112.695273],
    popup='Kejaksaan Negeri Surabaya',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.269375, 112.694663],
    popup='Loewy Boutique Salon',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.269207, 112.693760],
    popup='GBI Rock - Darmo Satelite Town',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.269373, 112.693653],
    popup='Cinazano Wine',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
    location=[-7.270716, 112.695149],
    popup='Sekolah Menengah Atas Kristen Gloria 1',
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(micin)

folium.Marker(
	location=[-7.339394, 112.738117],
    popup='Universitas Kristen Petra, Kampus Timur',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
	location=[-7.338958, 112.737522],
    popup='The Square Hotel',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
	location=[-7.339368, 112.735791],
    popup='Homestay Boss Alfian Bimantara Bintang 5',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
	location=[-7.339352, 112.736550],
    popup='Bank Mandiri',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
	location=[-7.340294, 112.736824],
    popup='Sekolah Dasar Negeri Siwalankerto III/420',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
	location=[-7.341233, 112.738755],
    popup='Multi Futsal',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
	location=[-7.342435, 112.739560],
    popup='Crystal X Waru Surabaya',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
	location=[-7.342802, 112.739289],
    popup='MILLENIUM SURABAYA Tempat Percetakan Dan Barang Promosi',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
	location=[-7.342493, 112.740220],
    popup='RjP99 Cell',
    icon=folium.Icon(color='green')
).add_to(micin)

folium.Marker(
	location=[-7.342927, 112.740180],
    popup='Toko Jadi Jaya',
    icon=folium.Icon(color='green')
).add_to(micin)

micin

folium.Marker([-7.340332, 112.732804], popup='<i>SANJAYA TAMA LESTARI SURABAYA</i>').add_to(bocah)
folium.Marker([-7.241431, 112.730339], popup='<i>Balai Besar Teknik Kesehatan Lingkungan dan Pengendalian Penyakit</i>').add_to(bocah)
folium.Marker([-7.242176, 112.730189], popup='<i>Surabaya Meka Box. PT</i>').add_to(bocah)
folium.Marker([-7.240335, 112.731412], popup='<i>Museum Kesehatan Dr. Adhyatma, MPH</i>').add_to(bocah)
folium.Marker([-7.242485, 112.731798], popup='<i>Damai</i>').add_to(bocah)
folium.Marker([-7.340332, 112.732804], popup='<i>KPPN Surabaya I</i>').add_to(bocah)
folium.Marker([-7.242346, 112.733075], popup='<i>Gedung Keuangan Negara I Surabaya</i>').add_to(bocah)
folium.Marker([-7.243027, 112.732367], popup='<i>Kemayoran Baru Buntu No 41</i>').add_to(bocah)
folium.Marker([-7.243336, 112.733783], popup='<i>Kejaksaan Negeri Tanjung Perak</i>').add_to(bocah)
folium.Marker([-7.340332, 112.732804], popup='<i>Museum Kesehatan Dr. Adhyatma, MPH</i>').add_to(bocah)
folium.Marker([-7.241889, 112.735693], popup='<i>Sekolah Dasar Katolik Santa Angela</i>').add_to(bocah)

folium.Marker([-7.309107, 112.813915], popup='<i>Green Semanggi Mangrove</i>').add_to(bocah)
folium.Marker([-7.306799, 112.811660], popup='<i>Perumahan greenlake</i>').add_to(bocah)
folium.Marker([-7.304594, 112.810487], popup='<i>Modifikasi Striping Motor</i>').add_to(bocah)
folium.Marker([-7.304702, 112.809296], popup='<i>Bumi Wonorejo Asri</i>').add_to(bocah)
folium.Marker([-7.304451, 112.807726], popup='<i>Perm Grand Semanggi Residence</i>').add_to(bocah)
folium.Marker([-7.306742, 112.809422], popup='<i>Green Lake Natural Living</i>').add_to(bocah)
folium.Marker([-7.308406, 112.809332], popup='<i>Gardu Induk Surabaya Selatan</i>').add_to(bocah)
folium.Marker([-7.309015, 112.808159], popup='<i>Wisata Semanggi HERY</i>').add_to(bocah)
folium.Marker([-7.303073, 112.800454], popup='<i>Lingkungan Pondok Sosial (Liponsos) Surabaya</i>').add_to(bocah)
folium.Marker([-7.303986, 112.800671], popup='<i>TPU Keputih</i>').add_to(bocah)

folium.Marker([-7.266493, 112.691887], popup='<i>Lucky Mart & Healthy Care</i>').add_to(bocah)
folium.Marker([-7.266640, 112.691216], popup='<i>Rumah Sakit Mitra Keluarga Surabaya</i>').add_to(bocah)
folium.Marker([-7.266041, 112.689616], popup='<i>Debs Cake Surabaya</i>').add_to(bocah)
folium.Marker([-7.264645, 112.690240], popup='<i>Super Indo Satelit Utara</i>').add_to(bocah)
folium.Marker([-7.266311, 112.691786], popup='<i>Bakso Panjul</i>').add_to(bocah)
folium.Marker([-7.266332, 112.691726], popup='<i>Mushola RS Mitra Keluarga Satelit</i>').add_to(bocah)

folium.Marker([-7.342260, 112.718425], popup='<i>Warung Maksol</i>').add_to(bocah)
folium.Marker([-7.340600, 112.717289], popup='<i>Triple C</i>').add_to(bocah)
folium.Marker([-7.335652, 112.712167], popup='<i>PITURAGA</i>').add_to(bocah)
folium.Marker([-7.335433, 112.711780], popup='<i>SMPN 55 Surabaya</i>').add_to(bocah)
folium.Marker([-7.335487, 112.711571], popup='<i>Kedai Kopi 55</i>').add_to(bocah)
folium.Marker([-7.336931, 112.712086], popup='<i>Warung Ngawang</i>').add_to(bocah)
folium.Marker([-7.337043, 112.712162], popup='<i>Bakso Iga Sapu Two Nine</i>').add_to(bocah)
folium.Marker([-7.334217, 112.712664], popup='<i>UPT PMP2KP Surabaya</i>').add_to(bocah)
folium.Marker([-7.332916, 112.713223], popup='<i>Toko Hidayah</i>').add_to(bocah)
folium.Marker([-7.332920, 112.712030], popup='<i>Dinas Pertanian Kota Surabaya</i>').add_to(bocah)

folium.Marker([-7.201499, 112.734490], popup='<i>PT Panca Pilar Tangguh</i>').add_to(bocah)
folium.Marker([-7.201557, 112.734147], popup='<i>Pt. Jangkar Pacific</i>').add_to(bocah)
folium.Marker([-7.201832, 112.733535], popup='<i>Sepinggan Indah Travel</i>').add_to(bocah)
folium.Marker([-7.202278, 112.733856], popup='<i>Tanjung Redeb Indah Perkasa</i>').add_to(bocah)
folium.Marker([-7.202373, 112.734574], popup='<i>Pt. Karya Indah Transindo</i>').add_to(bocah)
folium.Marker([-7.202556, 112.733749], popup='<i>PT Portek Indonesia</i>').add_to(bocah)
folium.Marker([-7.202965, 112.733385], popup='<i>PT. Tehnik Agung Jaya</i>').add_to(bocah)
folium.Marker([-7.202376, 112.734984], popup='<i>KOPERASI TKBM USAHA KARYA</i>').add_to(bocah)
folium.Marker([-7.203777, 112.733243], popup='<i>PGN SAKA</i>').add_to(bocah)
folium.Marker([-7.204708, 112.732519], popup='<i>Terminal Mirah</i>').add_to(bocah)

folium.Marker([-7.254068, 112.803550], popup='<i>Tugu</i>').add_to(bocah)
folium.Marker([-7.253220, 112.802621], popup='<i>Atlantis Land Kenjeran</i>').add_to(bocah)
folium.Marker([-7.251707, 112.803526], popup='<i>Kenpark</i>').add_to(bocah)
folium.Marker([-7.250889, 112.800961], popup='<i>Pantai Ria Kenjeran</i>').add_to(bocah)
folium.Marker([-7.252716, 112.797777], popup='<i>Lampung Kobo</i>').add_to(bocah)
folium.Marker([-7.248768, 112.798853], popup='<i>Batle Land Or Shoting Target</i>').add_to(bocah)
folium.Marker([-7.248096, 112.798985], popup='<i>Waterpark Kenjeran</i>').add_to(bocah)
folium.Marker([-7.247324, 112.801067], popup='<i>Patung Buddha 4 Rupa</i>').add_to(bocah)
folium.Marker([-7.244107, 112.797721], popup='<i>Bekas Wisata Pantai Kulon</i>').add_to(bocah)
folium.Marker([-7.247134, 112.802526], popup='<i>Vihara Dewi Kwan Im</i>').add_to(bocah)

bocah

simpan(bocahmicin,'micin1.html')
simpan(micin,'micin2.html')
simpan(bocah,'micin3.html')
