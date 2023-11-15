/*
当前版本：2.1
*/

package main

import (
	"fmt"
	"log"
	"os"
	"qiandaodog/src/models"
	"strings"
)

func GetCookiesFromEnv() (cookie []string, err error) {
	// Assuming you set a GitHub Actions secret named COOKIES with the cookie values
	cookiesEnv, exists := os.LookupEnv("COOKIES")
	if !exists || cookiesEnv == "" {
		return nil, fmt.Errorf("COOKIES environment variable not set")
	}

	return strings.Split(cookiesEnv, ";"), nil
}

func StringSplitn(s1, s2 string) ([]string, error) {
	r1 := strings.SplitAfterN(s1, s2, 10)
	if len(r1) != 2 {
		return r1, fmt.Errorf("Array Not slice")
	}
	r1[1] = strings.Replace(r1[1], "\r", "", -1)
	r1[1] = strings.Replace(r1[1], "\n", "", -1)
	return r1, nil
}

func main() {
	txtbody, err := GetCookiesFromEnv()
	if err != nil {
		log.Fatal(err)
	}

	t := len(txtbody)
	for i := 0; i < t; i++ {
		CookieBool, err := StringSplitn(txtbody[i], `"=`)
		if err != nil || CookieBool[1] == "" {
			continue
		}
		switch CookieBool[0] {
		case `"v2ex"=`: //V2EX
			c := &models.V2exCookie{}
			c.Cookies = CookieBool[1]
			c.SetV2ex()
		case `"163music"=`: //网易云音乐
			c := &models.Music163Cookie{}
			c.Cookies = CookieBool[1]
			c.SetMusic163()
		case `"chh"=`: //CHH
			c := &models.ChhCookie{}
			c.Cookies = CookieBool[1]
			c.SetChh()
		}
	}
}
