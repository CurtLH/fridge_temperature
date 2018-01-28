# fridge_temperature

Have you ever wondered why sometimes why sometimes when you take your ice cream out of the freezer it's harder than other times? To say that thought has crossed my mind once or twice would be an understatement!

Using my Raspberry Pi and a few DS18B20 sensors, I was able to put together something that would allow me to record room temperature, refrigerator temperature, and freezer temperature. Every 30 seconds, the temperature was taken and the values were inserted into a PostgreSQL database.

<p align="center"> 
<img src="https://github.com/CurtLH/fridge_temperature/blob/master/hardware.png">
</p>

After collecting data for a couple of days, I was then able to put the results into `R` and start to investigate what is happening with the temperature in my refrigerator. As seen in the graphic below, the temperature in both the refrigerator and freezer continuously vary by nearly 20 degrees. I expected some variation, but definitely not 20 degrees! 

<p align="center"> 
<img src="https://github.com/CurtLH/fridge_temperature/blob/master/chart.png">
</p>

Now I don't know if this is normal or not, so my next steps are to ask a couple friends if I can place sensors in their refrigerators for a few days and see how it compares.
