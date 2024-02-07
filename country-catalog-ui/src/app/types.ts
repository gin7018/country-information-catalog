
export interface CountryName {
    name: string;
    iso_code: string;
}

export interface CountryProfile {
    name: string;
    iso_code: string;
    capital_city: string;
    country_flag: string;
    languages: string[];
}

export interface Place {
    name: string;
    address: string;
    phone: string;
    url: string;
}
