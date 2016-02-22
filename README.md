# TS_LPS
Estimate expected log rate based on CPS stats from tech support file.

This script will scrape the provided tech support file for CPS information and is intended for use with evaluation systems (where all policies are logged). If used for an existing customer, be aware that the script assumes all policies are generating logs (and will be forwarding to Panorama) and estimates only traffic logs. Representative traffic mixes show a 70%/30% of traffic & threat for planning purposes.

Usage: "./ts_lps.py"



If you have any issues, please contact cstancill@paloaltonetworks.com
