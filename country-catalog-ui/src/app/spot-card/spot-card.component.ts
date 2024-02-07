import {Component, Input, OnInit} from '@angular/core';
import {Place} from "../types";

@Component({
  selector: 'app-spot-card',
  templateUrl: './spot-card.component.html',
  styleUrls: ['./spot-card.component.css']
})
export class SpotCardComponent implements OnInit {
  @Input() spot: Place | undefined;

  constructor() { }

  ngOnInit(): void {
  }

}
