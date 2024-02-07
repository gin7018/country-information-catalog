import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";


@Injectable({
  providedIn: 'root'
})
export class CatalogServiceService {
  private port = 'http://127.0.0.1:5000/';

  constructor(private http: HttpClient) { }

  fetch_all_countries(): Observable<any[]> {
    const endpoint_url = this.port + 'country/all';
    return this.http.get<any[]>(endpoint_url)
  }

  fetch_country_profile(country_code: string): Observable<any> {
    const endpoint = this.port + `country/profile/${country_code}`
    return this.http.get<any>(endpoint)
  }

  convert_currency(to: string, from: string, amount: number): Observable<number> {
    const endpoint = new URL(this.port + `currency/convert/`);
    endpoint.searchParams.set("from_currency", from);
    endpoint.searchParams.set("to_currency", to);
    endpoint.searchParams.set("amount", String(amount));

    return this.http.get<number>(endpoint.toString());
  }

  fetch_tourist_attractions_in_country(country_code: string): Observable<any[]> {
    const endpoint = this.port + `places/tourist/${country_code}`
    return this.http.get<any[]>(endpoint)
  }

  fetch_restaurants_in_country(country_code: string): Observable<any[]> {
    const endpoint = this.port + `places/restaurants/${country_code}`
    return this.http.get<any[]>(endpoint)
  }



}
