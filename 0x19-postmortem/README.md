# Postmortem: Installing Nginx on the Web Server (A Cautionary Tale)

## Issue Summary

Duration: 2 hours, 11:00 AM to 1:00 PM (UTC-5)

Impact: The web server went on strike and took an unscheduled break, leaving 100% of users unable to access the website.

Root cause: Failed installation of Nginx on the web server due to a missing dependency.

## Timeline

- 11:00 AM: Our monitoring alerts started ringing like crazy, telling us that something was wrong with the web server.
- 11:05 AM: Our engineer, Bob, noticed the issue and started investigating. Bob is a great engineer, but he also has a short attention span and loves to chase shiny objects.
- 11:15 AM: Bob got distracted by a shiny object and assumed that the root cause was related to the web server configuration files. He spent the next 15 minutes chasing his tail in the config files.
- 11:30 AM: Bob tried to restart the web server, hoping that it would fix the issue. It didn't. Oops.
- 11:45 AM: Bob thought it might be a hardware issue and started inspecting the server hardware. He found nothing and realized he'd been barking up the wrong tree.
- 12:00 PM: Bob escalated the issue to the server administration team, who quickly identified the missing dependency issue and started working on a fix.
- 12:30 PM: The software development team swooped in like a superhero team to fix the issue and save the day.
- 1:00 PM: The web server was finally back online, and Bob was left feeling a little embarrassed.

### This is Bob after the issue was resolved :)
![Bob](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmzsi6RWNZ4bQ1sftHI4s-SFRxjzpVcJpF1g&usqp=CAU)

## Root cause and resolution

Root cause: The failed installation of Nginx was caused by a missing dependency that was not installed before attempting to install Nginx. It turns out that Bob forgot to feed Nginx its favorite snack before trying to install it.

Resolution: The software development team installed the missing dependency and successfully installed Nginx on the web server, with a side of Nginx's favorite snack, of course.

## Corrective and preventative measures

### Improvement

- Bob has been instructed to avoid shiny objects and focus on the task at hand.
- We'll improve our installation processes to ensure all dependencies are installed before attempting to install any software on the web server.
- We'll make sure to have plenty of Nginx's favorite snack on hand for all future installations.

### Tasks

- We'll patch the Nginx server with the latest security updates to make sure it's happy and healthy.
- We'll add monitoring on server memory and CPU usage to detect potential hardware issues before they cause any more mischief.
- We'll review and improve our web server configuration files to prevent future configuration-related issues. Bob will be supervised during this process.

## Conclusion

Installing Nginx on the web server was a wild ride, with Bob chasing shiny objects and Nginx going on strike. We eventually identified the root cause and fixed the issue, but not before the web server took an unscheduled break. We've learned our lesson and will be improving our processes to prevent similar issues from occurring in the future. And we'll always make sure to have plenty of Nginx's favorite snack on hand.

