import {Component, OnInit} from '@angular/core';
import {CatalogServiceService} from "./catalog-service.service";
import {CountryName, CountryProfile, Currency, Place} from "./types";

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

  selected_country_currency: Currency = {
    name: 'Dollar',
    iso_code: 'USD'
  };

  selected_currency_value = 1;
  usd_value = 1;
  convertion_rate = 1.0;

  selected_country_tourist_spots: Place[] = [
    {
      name: 'Ponte',
      address: 'Quissoma, Uíge',
      phone: '+1 222-222-222',
      url: ''
    }
  ];
  selected_country_restaurant_spots: Place[] = [
    {
      name: 'Restaurante Lafil',
      address: 'Samba, Luanda',
      phone: '+1 222-222-222',
      url: 'lafil.com/hours'
    }
  ];


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

    this.selected_currency_value = 1;
    this.usd_value = 1;

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

        this.catalog_service.fetch_country_currency(country_code)
          .subscribe(currency => this.selected_country_currency = currency as Currency)
      });

  }

  convert_currency(from_currency: string, to_currency: string, amount: number): void {
    this.catalog_service.convert_currency(from_currency, to_currency, amount)
      .subscribe( conversion_result => {
        if (to_currency == this.selected_country_currency.iso_code) {
          this.selected_currency_value = conversion_result;
        }
        else {
          this.usd_value = conversion_result;
        }
        })
  }

}

