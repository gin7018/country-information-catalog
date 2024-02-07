import {Component, OnInit} from '@angular/core';
import {CatalogServiceService} from "./catalog-service.service";
import {CountryName, CountryProfile, Place} from "./types";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  country_list: CountryName[] = [];

  selected_country_info = {
    name: 'Angola',
    capital_city: 'Luanda',
    country_flag: 'img',
    languages: ['English', 'French']
  }

  selected_country_tourist_spots: Place[] = [];
  selected_country_restaurant_spots: Place[] = [];


  constructor(private catalog_service: CatalogServiceService) {
  }

  ngOnInit(): void {
    this.fetch_all_countries();
  }

  fetch_all_countries(): void {
    this.country_list = [];
    this.catalog_service.fetch_all_countries()
      .subscribe(
        countries => {
          for (let country of countries) {
            let rep = JSON.parse(country) as CountryName;
            this.country_list.push(rep);
          }
        }
      );
  }

  fetch_country_profile(country_code: string): void {
    this.selected_country_tourist_spots = [];
    this.selected_country_restaurant_spots = [];
    this.catalog_service.fetch_country_profile(country_code)
      .subscribe(country_profile => {
        this.selected_country_info = country_profile as CountryProfile;

        this.catalog_service.fetch_tourist_attractions_in_country(country_code)
          .subscribe(spots => {
            for (let el of spots.slice(0, 5)) {
              let obj = JSON.parse(el) as Place;
              this.selected_country_tourist_spots.push(obj);
            }
          });

        this.catalog_service.fetch_restaurants_in_country(country_code)
          .subscribe(spots => {
            for (let el of spots.slice(0, 5)) {
              let obj = JSON.parse(el) as Place;
              this.selected_country_restaurant_spots.push(obj);
            }
          });
      });

  }

}

