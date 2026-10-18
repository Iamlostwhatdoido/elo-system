extends Node

# Expenctancy Parameters
const STANDARD_GAP: int = 400
const EXPECTANCY_BASE: int = 9
const CORRECTION: float = log(EXPECTANCY_BASE)/STANDARD_GAP


const DEFAULT_SCORE: int = 0
const MAX_DOUBT: int = 350
const MIN_DOUBT: int = 30

const FORGET_DAYS: int = 365
const TIME_COEF: float = (MAX_DOUBT**2 - MIN_DOUBT**2)/float(FORGET_DAYS)

const DEFAULT_IMAGE_PATH := "res://assets/BrokenImage.png"
var DEFAULT_IMAGE_BUFFER := FileManager.create_buffer_from_image(DEFAULT_IMAGE_PATH)
const SAVE_PATH := "res://saves/"
