#!/bin/python

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
