#!/bin/python

import folium

indrarh = folium.Map(
    location=[-7.3044144,112.7412095],
    zoom_start=12,
    tiles='Stamen Terrain'
)

folium.Marker([-7.296218, 112.738667], popup='<b>Surabaya Zoo</b>').add_to(indrarh)
folium.Marker([-7.265440, 112.750301], popup='<b>Monumem Kapal Selam Surabaya</b>').add_to(indrarh)
folium.Marker([-7.264820, 112.750417], popup='<b>Moncafe (Monkasel Caffe)</b>').add_to(indrarh)
folium.Marker([-7.263952, 112.750346], popup='<b>Skate Park Surabaya</b>').add_to(indrarh)
folium.Marker([-7.262582, 112.748980], popup='<b>Sekolah Nasional Tiga Bahasa Little Sun School</b>').add_to(indrarh)
folium.Marker([-7.262865, 112.748857], popup='<b>Sasana Wushu YASANIS</b>').add_to(indrarh)
folium.Marker([-7.264150, 112.749183], popup='<b>Embassy English Centre</b>').add_to(indrarh)
folium.Marker([-7.268390, 112.747916], popup='<b>KPP Pratama Surabaya Genteng</b>').add_to(indrarh)
folium.Marker([-7.268040, 112.747812], popup='<b>The WIN Hotel Surabaya</b>').add_to(indrarh)
folium.Marker([-7.268312, 112.747679], popup='<b>Masjid An Nur (Kantor Pajak)</b>').add_to(indrarh)

indrarh

kh = folium.Map(
    location=[-7.3044144,112.7412095],
    zoom_start=12,
    tiles='Stamen Terrain'
)

folium.Marker([-7.258340, 112.751175], popup='<b>Kampoeng Stik</b>').add_to(kh)
folium.Marker([-7.257855, 112.751642], popup='<b>Sachman Surabaya</b>').add_to(kh)
folium.Marker([-7.257309, 112.749175], popup='<b>Sekolah Menengah Atas Negeri 1 Surabaya</b>').add_to(kh)
folium.Marker([-7.257005, 112.749230], popup='<b>Sekolah Menengah Atas Negeri 2 Surabaya</b>').add_to(kh)
folium.Marker([-7.257387, 112.748216], popup='<b>Kantor Bappeko Surabaya</b>').add_to(kh)
folium.Marker([-7.257807, 112.747708], popup='<b>Dinas Kominfo Surabaya</b>').add_to(kh)
folium.Marker([-7.257893, 112.748220], popup='<b>Masjid Al Muhajirin</b>').add_to(kh)
folium.Marker([-7.257302, 112.746237], popup='<b>Hotel Royal Regal Surabaya</b>').add_to(kh)
folium.Marker([-7.258302, 112.748605], popup='<b>My Grill Surabaya</b>').add_to(kh)
folium.Marker([-7.259627, 112.746969], popup='<b>Kantor Walikota Surabaya</b>').add_to(kh)

kh

n = folium.Map(
    location=[-7.3044144, 112.7412095],
    zoom_start=12,
    tiles='Stamen Terrain'
)

folium.Marker(
    location=[-7.229636, 112.766269],
    popup='Sidotopo Wetan',
    icon=folium.Icon(icon='cloud')
).add_to(n)

folium.Marker(
    location=[-7.280613, 112.770057],
    popup='KFC Manyar',
    icon=folium.Icon(color='green')
).add_to(n)

folium.Marker(
    location=[-7.279612, 112.766720],
    popup='Pizza Hut Manyar',
    icon=folium.Icon(color='red', icon='info')
).add_to(n)

folium.Marker(
    location=[-7.277314, 112.766087],
    popup='Boncafe Manyar',
    icon=folium.Icon(color='red', icon='info')
).add_to(n) 

folium.Marker(
    location=[-7.280176, 112.768930],
    popup='Ayam Bakar Primarasa',
    icon=folium.Icon(color='red', icon='info')
).add_to(n) 

folium.Marker(
    location=[-7.278272, 112.766549],
    popup='Ikan Bakar Cianjur',
    icon=folium.Icon(color='green')
).add_to(n)

folium.Marker(
    location=[-7.278921, 112.765476],
    popup='Bonet Supermarket',
    icon=folium.Icon(icon='cloud')
).add_to(n)

folium.Marker(
    location=[-7.280113, 112.766120],
    popup='Hakata Ikkousha',
    icon=folium.Icon(icon='cloud')
).add_to(n)

folium.Marker(
    location=[-7.279868, 112.764027],
    popup='Gramedia Manyar',
    icon=folium.Icon(color='red', icon='info')
).add_to(n) 

folium.Marker(
    location=[-7.280102, 112.772460],
    popup='BCA KCP Kertajaya',
    icon=folium.Icon(color='red', icon='info')
).add_to(n) 

n


n = folium.Map(
    location=[-7.3044144, 112.7412095],
    zoom_start=12,
    tiles='Stamen Terrain'
)

folium.Marker(
    location=[-7.313033, 112.728353],
    popup='Bank BTN',
    icon=folium.Icon(color='chocolate')
).add_to(n)

folium.Marker(
    location=[-7.312661, 112.727430],
    popup='Gedung GEMA UNESA',
    icon=folium.Icon(color='green')
).add_to(n)

folium.Marker(
    location=[-7.311842, 112.726593],
    popup='Pascasarjana Unesa',
    icon=folium.Icon(color='red')
).add_to(n)

folium.Marker(
    location=[-7.314024, 112.727618],
    popup='Lapangan UNESA',
    icon=folium.Icon(color='pink')
).add_to(n) 


folium.Marker(
    location=[-7.314168, 112.726180],
    popup='RanUnesa',
    icon=folium.Icon(color='gray')
).add_to(n) 


folium.Marker(
    location=[-7.314370, 112.726754],
    popup='Kafe Unesa',
    icon=folium.Icon(color='black')
).add_to(n) 


folium.Marker(
    location=[-7.314583, 112.727419],
    popup='UNESA Library',
    icon=folium.Icon(color='yellow')
).add_to(n) 

folium.Marker(
    location=[-7.314748, 112.728095],
    popup='Pusat Bahasa Universitas Negeri Surabaya',
    icon=folium.Icon(color='light green')
).add_to(n) 

folium.Marker(
    location=[-7.313785, 112.725343],
    popup='Masjid Unesa Ketintang',
    icon=folium.Icon(color='blue')
).add_to(n) 

folium.Marker(
    location=[-7.315482, 112.724560],
    popup='Unesa University Press',
    icon=folium.Icon(color='light blue')
).add_to(n) 

folium.Marker(
    location=[-7.315812, 112.724372],
    popup='Lembaga Penjaminan Mutu Pendidikan (LPMP) Jawa Timur',
    icon=folium.Icon(color='dark blue')
).add_to(n) 

folium.Marker(
    location=[-7.316047, 112.748636],
    popup='Plasa Marina Surabaya',
    icon=folium.Icon(color='chocolate')
).add_to(n)

folium.Marker(
    location=[-7.316003, 112.748831],
    popup='Adira',
    icon=folium.Icon(color='green')
).add_to(n)

folium.Marker(
    location=[-7.315823, 112.748923],
    popup='Axioo',
    icon=folium.Icon(color='gold')
).add_to(n)

folium.Marker(
    location=[-7.316344, 112.748537],
    popup='Galeri Indosat Plaza Marina',
    icon=folium.Icon(color='pink')
).add_to(n) 


folium.Marker(
    location=[-7.316738, 112.748698],
    popup='BII ATM Sinar Fontana Surabaya',
    icon=folium.Icon(color='gray')
).add_to(n) 


folium.Marker(
    location=[-7.316344, 112.748210],
    popup='McDonalds',
    icon=folium.Icon(color='black')
).add_to(n) 


folium.Marker(
    location=[-7.315937, 112.748605],
    popup='HokBen Plasa Marina',
    icon=folium.Icon(color='yellow')
).add_to(n) 

folium.Marker(
    location=[-7.316298, 112.748005],
    popup='Samsung Partner Plaza - PEACE CELL - PLASA MARINA',
    icon=folium.Icon(color='green')
).add_to(n) 

folium.Marker(
    location=[-7.316024, 112.749291],
    popup='Parkir Timur Plaza Marina',
    icon=folium.Icon(color='blue')
).add_to(n) 

folium.Marker(
    location=[-7.315294, 112.748474],
    popup='Apartemen Puncak Marina Tower 1',
    icon=folium.Icon(color='blue')
).add_to(n) 
n


bocahmicin = folium.Map(
    location=[-7.3044144, 112.7412095],
    zoom_start=12,
    tiles='Stamen Terrain'
)

folium.Marker(
    location=[-7.222785, 112.735106],
    popup='Tokoraket.com',
    icon=folium.Icon(color='purple')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.220992, 112.732998 ],
    popup='Perak Photo',
    icon=folium.Icon(color='white')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.221663, 112.731764 ],
    popup='PT. Pelayaran Meratus',
    icon=folium.Icon(color='red')
).add_to(bocahmicin)

folium.Marker(
    location=[-7.218842, 112.730257 ],
    popup='GAMA-Group',
    icon=folium.Icon(color='gray')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.215881, 112.729800 ],
    popup='Sami Jaya',
    icon=folium.Icon(color='pink')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.214343, 112.728389 ],
    popup='Toko Abrilia',
    icon=folium.Icon(color='black')
).add_to(bocahmicin) 


folium.Marker(
    location=[-7.213327, 112.727268 ],
    popup='Yonif 1 Marinir',
    icon=folium.Icon(color='yellow')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.210098, 112.723294 ],
    popup='Cumi Hitam 19',
    icon=folium.Icon(color='light green')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.210042, 112.722781 ],
    popup='Pelni Surya',
    icon=folium.Icon(color='blue')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.206868, 112.721786 ],
    popup='PT. Petro Andalan Nusantara',
    icon=folium.Icon(color='light blue')
).add_to(bocahmicin) 

folium.Marker(
    location=[-7.198897, 112.731820],
    popup='Terminal Jamrud',
    icon=folium.Icon(color='dark blue')
).add_to(bocahmicin) 
bocahmicin
