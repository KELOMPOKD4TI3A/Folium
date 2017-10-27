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
